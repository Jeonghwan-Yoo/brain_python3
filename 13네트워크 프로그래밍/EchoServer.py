#>EchoServer.py <Bind IP>
import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('클라이언트 접속 : {0}'.format(self.client_address[0]))
        sock=self.request

        rbuff=sock.recv(1024) #데이터를 수신하고 그결과를 rbuff에 담습니다. bytes형식.
        received=str(rbuff,encoding="utf-8")
        print('수신 : {0}'.format(received))

        #수신한 데이터를 그대로 돌려보냄.
        sock.send(rbuff) #수신한 데이터를 그대로 클라이언트에게 다시 송신.
        print('송신 : {0}'.format(received))
        sock.close()

if __name__=='__main__':
    if len(sys.argv)<2:
        print('{0} <Bind IP>'.format(sys.argv[0]))
        sys.exit()
    
    bindIP=sys.argv[1]
    bindPort=5425

    #IP와 포트번호를 담은 튜플과 파생클래스를 매개변수로 넘김.
    server=socketserver.TCPServer((bindIP,bindPort),MyTCPHandler)

    print('메아리 서버 시작...')
    server.serve_forever() #클라이언트로부터 접속 요청을 받아들일 준비
