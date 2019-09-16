import os
import sys
import socket
import socketserver
import struct

import message
from message import Message

from message_header import Header
from message_body import BodyData
from message_body import BodyRequest
from message_body import BodyResponse
from message_body import BodyResult

from message_util import MessageUtil

CHUNK_SIZE = 4096
upload_dir = ''

class FileReceiveHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("클라이언트 접속 : {0}".format(self.client_address[0]))

        client = self.request # client socket

        #클라이언트가 보내온 파일 전송 요청 메시지를 수신합니다.
        reqMsg = MessageUtil.receive(client) 

        if reqMsg.Header.MSGTYPE != message.REQ_FILE_SEND:
            client.close()
            return

        reqBody = BodyRequest(None)

        print(
            "파일 업로드 요청이 왔습니다. 수락하시겠습니까? yes/no")
        answer = sys.stdin.readline()

        rspMsg = Message()
        rspMsg.Body = BodyResponse(None)
        rspMsg.Body.MSGID = reqMsg.Header.MSGID
        rspMsg.Body.RESPONSE = message.ACCEPTED

        rspMsg.Header = Header(None)

        msgId = 0
        rspMsg.Header.MSGID = msgId
        msgId = msgId + 1
        rspMsg.Header.MSGTYPE = message.REP_FILE_SEND
        rspMsg.Header.BODYLEN = rspMsg.Body.GetSize()
        rspMsg.Header.FRAGMENTED = message.NOT_FRAGMENTED
        rspMsg.Header.LASTMSG = message.LASTMSG
        rspMsg.Header.SEQ = 0

        if answer.strip() != "yes": #yes가 아닌 답을 입력하면 '거부'응답
            rspMsg.Body = BodyResponse(None)
            rspMsg.Body.MSGID = reqMsg.Header.MSGID
            rspMsg.Body.RESPONSE = message.DENIED
        
            MessageUtil.send(client, rspMsg)
            client.close()
            return
        else: #yes면 '승락'응답
            MessageUtil.send(client, rspMsg)

            print("파일 전송을 시작합니다...")

            fileSize = reqMsg.Body.FILESIZE
            fileName = reqMsg.Body.FILENAME
            recvFileSize = 0 
            #업로드받을 파일을 생성합니다.
            with open(upload_dir + "\\" + fileName, 'wb') as file:
                dataMsgId = -1
                prevSeq = 0
                
                while True:
                    reqMsg = MessageUtil.receive(client)
                    if reqMsg == None:
                        break

                    print("#", end='')
                    
                    if reqMsg.Header.MSGTYPE != message.FILE_SEND_DATA:
                        break

                    if dataMsgId == -1:
                        dataMsgId = reqMsg.Header.MSGID
                    elif dataMsgId != reqMsg.Header.MSGID:
                        break                    

                    if prevSeq != reqMsg.Header.SEQ: #메시지 순서가 어긋나면 중단.
                        print("{0}, {1}".format(prevSeq, reqMsg.Header.SEQ))
                        break
                    
                    prevSeq += 1

                    #전송받은 파일의 일부를 담고 있는 bytes객체를
                    #서버에서 생성한 파일에 기록합니다.
                    recvFileSize += reqMsg.Body.GetSize()
                    file.write(reqMsg.Body.GetBytes())

                    #마지막 메시지면 반복문을 빠져나옴.
                    if reqMsg.Header.LASTMSG == message.LASTMSG:
                        break
               
                file.close()

                print()
                print("수신 파일 크기 : {0} bytes".format(recvFileSize))

                rstMsg = Message()
                rstMsg.Body = BodyResult(None)
                rstMsg.Body.MSGID = reqMsg.Header.MSGID
                rstMsg.Body.RESULT = message.SUCCESS
                
                rstMsg.Header = Header(None)
                rstMsg.Header.MSGID = msgId
                msgId += 1
                rstMsg.Header.MSGTYPE = message.FILE_SEND_RES
                rstMsg.Header.BODYLEN = rstMsg.Body.GetSize()
                rstMsg.Header.FRAGMENTED = message.NOT_FRAGMENTED
                rstMsg.Header.LASTMSG = message.LASTMSG
                rstMsg.Header.SEQ = 0

                #파일 전송 요청에 담겨온 파일 크기와 실제 크기를 비교하여 같으면 성공.
                if fileSize == recvFileSize:
                    MessageUtil.send(client, rstMsg)
                else: #파일 크기에 이상이 있다면 실패 메시지를 보냅니다.
                    rstMsg.Body = BodyResult(None)
                    rstMsg.Body.MSGID = reqMsg.Header.MSGID
                    rstMsg.Body.RESULT = message.FAIL
                    MessageUtil.send(client, rstMsg)

            print("파일 전송을 마쳤습니다.")                
            client.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("사용법 : {0} <Directory>".format(sys.argv[0]))
        sys.exit(0)

    upload_dir = sys.argv[1]
    if os.path.isdir(upload_dir) == False:
        os.mkdir(upload_dir)
         
    bindPort = 5425 #서버 포트.
    server = None
    try:
        #IP주소를 ''로 입력하면 클라이언트는 서버 애플리케이션에 할당된 아무 주소나 가능.
        server = socketserver.TCPServer(('', bindPort), FileReceiveHandler)
            
        print("파일 업로드 서버 시작...")
        server.serve_forever()
    except Exception as err:
        print(err)

    print("서버를 종료합니다.")