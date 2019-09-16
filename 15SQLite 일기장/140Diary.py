from datetime import datetime
import sqlite3
import wx
import wx.html2 #WebView
import ntpath #파일 이름 추출
import base64 #이미지 URI 인코딩

RECORD_PER_PAGE=5 #한 페이지에 몇 건의 일기 레코드를 표시할지를 지정

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title="140자 일기장",
        size=wx.Size(715,655),style=wx.DEFAULT_FRAME_STYLE)
        
        self.MaxImageSize=200 #미리보기 이미지의 크기를 200*200넘지 않도록.
        
        self.mainPanel=wx.Panel(self)

        #일기 입력창
        self.leftPanel=wx.Panel(self.mainPanel)
        self.leftPanel.SetMaxSize(wx.Size(200,-1)) #-1은 크기 상관없을 때
        self.input_image_path=""
        self.inputTextCtrl=wx.TextCtrl(self.leftPanel, 
        size=wx.Size(200,100),style=wx.TE_MULTILINE) #\n을 줄바꿈으로 표시할 수 있다.
        
        self.inputTextCtrl.SetMaxLength(140) #일기장 텍스트 최대 길이 140.
        self.inputTextCtrl.Bind(wx.EVT_TEXT,self.OnTypeText)
        self.lengthStaticText=wx.StaticText(self.leftPanel,style=wx.ALIGN_RIGHT)
        self.selectImageButton=wx.Button(self.leftPanel,label="이미지 추가")
        self.selectImageButton.Bind(wx.EVT_BUTTON, self.OnFindImageFile)
        self.imageStaticBitmap=wx.StaticBitmap(self.leftPanel) #이미지 미리보기
        self.inputButton=wx.Button(self.leftPanel, label="저장")
        self.inputButton.Bind(wx.EVT_BUTTON,self.OnInputButton)

        #일기 표시 창
        self.rightPanel=wx.Panel(self.mainPanel)
        self.outputHtmlWnd=wx.html2.WebView.New(self.rightPanel)
        #일기 내용을 표시할 WebView객체를 정의.
        self.outputHtmlWnd.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnNavigating)

        #위젯 배치
        leftPanelSizer=wx.StaticBoxSizer(wx.VERTICAL,self.leftPanel,"글 남기기")
        leftPanelSizer.Add(self.inputTextCtrl,0,wx.ALL,5)
        leftPanelSizer.Add(self.lengthStaticText,0,wx.ALIGN_RIGHT|wx.RIGHT,5)
        leftPanelSizer.Add(self.selectImageButton,0,wx.ALIGN_RIGHT|wx.RIGHT,5)
        leftPanelSizer.Add(self.imageStaticBitmap,0,wx.ALIGN_RIGHT|wx.ALL,5)
        leftPanelSizer.Add(self.inputButton,0,wx.ALIGN_RIGHT|wx.RIGHT,5)
        self.leftPanel.SetSizer(leftPanelSizer)

        htmlWndSizer=wx.GridSizer(1,1,0,0)
        htmlWndSizer.Add(self.outputHtmlWnd,0,wx.ALL|wx.EXPAND,5)
        self.rightPanel.SetSizer(htmlWndSizer)
        self.rightPanel.Layout() #윈도우 크기 바꿀 때 자동호출되어 조절.
        htmlWndSizer.Fit(self.rightPanel) #사이즈 재조정.

        mainSizer=wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(self.leftPanel,1,wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND,5)
        mainSizer.Add(self.rightPanel,1,wx.ALL|wx.EXPAND,5)
        self.mainPanel.SetSizer(mainSizer)
        self.Layout()

        #Database 초기화
        self.conn=sqlite3.connect("minutediary.db")
        self.cursor=self.conn.cursor()
        self.CheckSchema() #minutediary.db에 스키마를 생성하고
        self.LoadDiary(0) #데이터베이스에서 레코드를 불러 WebView에 내용 출력.

    def CheckSchema(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS DIARY(
        DIARY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CREATEDATE DATETIME,
        NOTE CHAR(140))
        """)
        
        #IF NOT EXISTS는 있으면 냅두고 없으면 만들라는 말
        #데이터 타입크기를 꼭 설정할 필욘 없다.
        #AUTOINCREMENT을 해주면 자동 생성된다.

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS DIARY_IMG(
        IMG_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        IMG BLOB,
        DIARY_ID INTERGER,
        FOREIGN KEY(DIARY_ID) REFERENCES DIARY(DIARY_ID))
        """)

        #생성하려는 테이블의 DIARY_ID를 DIARY테이블의 DIARY_ID를 참조하는 외래키로 지정.

    def OnTypeText(self, event):
        self.lengthStaticText.SetLabel(
            "현재 글자 수:{0}".format(len(self.inputTextCtrl.GetValue()))
        )
        self.leftPanel.Layout() #텍스트가 달라지면 위젯의 크기도 변합니다. 위젯을 재배치.
        
    def OnFindImageFile(self, event):
        #wx.FileDialog의 인스턴스를 생성.
        openFileDialog=wx.FileDialog(
            self,"Open",
            wildcard="Image files(*.png,*.jpg,*.gif)|*.png;*.jpg;*.jpeg;*.gif",
            style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)

        if openFileDialog.ShowModal()==wx.ID_OK:
            self.input_image_path=openFileDialog.GetPath()

            #비율을 유지하면서 이미지 크기를 윈도우에 맞추기
            #openFileDialog를 통해 얻어온 이미지 파일을 wx.Image객체를 통해 엽니다.
            img=wx.Image(self.input_image_path, wx.BITMAP_TYPE_ANY)
            Width=img.GetWidth()
            Height=img.GetHeight()
            if Width>Height:
                NewWidth=self.MaxImageSize
                NewHeight=self.MaxImageSize*Height/Width
            else:
                NewWidth=self.MaxImageSize
                NewHeight=self.MaxIamgeSize*Width/Height
            
            #Scale()메소드를 통해 Image객체의 크기를 조정합니다.
            img=img.Scale(NewWidth, NewHeight)
            #조정된 이미지 객체를 imageStaticBitmap에 지정
            self.imageStaticBitmap.SetBitmap(wx.Bitmap(img))
            self.leftPanel.Layout()
            self.leftPanel.Refresh()

    def OnInputButton(self, event):
        fileName=ntpath.basename(self.input_image_path)
        #DIARY 테이블에 레코드를 추가
        self.cursor.execute("""
        INSERT INTO DIARY (DIARY_ID, CREATEDATE, NOTE) VALUES(NULL,?,?)
        """,(str(datetime.now()),self.inputTextCtrl.GetValue()))

        #DIARY테이블에 추가된 레코드의 DIARY_ID를 얻어옵니다.
        diary_id=self.cursor.lastrowid
        
        #경로를 받아오면 DIARY_IMG테이블에 레코드를 추가합니다.
        if self.input_image_path.strip()!="":
            self.cursor.execute("""
            INSERT INTO DIARY_IMG (IMG_ID, IMG, DIARY_ID) VALUES(NULL,?,?)
            """,(sqlite3.Binary(open(self.input_image_path,"rb").read()),diary_id))
        
        self.conn.commit()

        wx.MessageBox("저장되었습니다.","140자 일기장", wx.OK)

        #일기 내용을 입력한 후에는 변수와 위젯을 초기화.
        self.inputTextCtrl.SetValue("")
        self.input_image_path=""
        self.imageStaticBitmap.SetBitmap(wx.Bitmap(0,0))

        #레코드 입력 후에는 LoadDiary()메소드를 호출해서 사용자에게 일기내용을 보여줌.
        self.leftPanel.Layout()
        self.leftPanel.Refresh()
        self.LoadDiary(0)

    def LoadDiary(self, page):
        #OUTER JOIN을 이용해 두 테이블에서 DIARY_ID가 같은 레코드를 조회하여 하나의 결과로
        #LIMIT은 최대 조회 건수, OFFSET은 읽어 들일 레코드의 순서를 지정.
        self.cursor.execute(
            "SELECT D.DIARY_ID, D.CREATEDATE, D.NOTE, I.IMG FROM DIARY AS D "
            +"LEFT OUTER JOIN DIARY_IMG AS I "
            +"ON D.DIARY_ID=I.DIARY_ID ORDER BY D.CREATEDATE DESC "
            +"LIMIT {0} OFFSET {1}".format(RECORD_PER_PAGE, page*RECORD_PER_PAGE)
        )
        
        html="""
        <html>
        <head>
        </head><body>{0}</body></html>
        """

        diary_id=0
        body=""
        for row in self.cursor:
            diary_id=int(row[0])
            imgTag=""
            #img가 있으면
            if row[3]:
                #이미지는 Base64인코딩을 통해 데이터 URI 스킴방식으로 HTML안에 삽입.
                imgTag="""<img src='data:image/png;base64,{0}'
                style='width:300px; height:auto;' align=center>
                """.format(base64.b64encode(row[3]).decode("ascii"))
            
            #삭제 링크에 DIARY_ID를 지정하고 [삭제]버튼의 하이퍼링크 주소는 "del:"로 시작.
            content="""<a name="neural">
            <p style="word-wrap:break-word;font-size=12px;">
            <font size=2><b><i>
            {1}
            </i></b>
            <a href="del:{0}">[삭제]</a></font><br>
            {2}
            <br>
            {3}""".format(diary_id, row[1],row[2], imgTag)

            body+=content
    
        pageNavigation="<p align='center' style='font-size=12px'>"

        #Prev 버튼(링크)
        if page>0:
            pageNavigation+="<a href='nav:{0}'>Prev</a>".format(page-1)
       
        #공백 문자를 연속으로 여러 개 삽입하고 싶을 경우. 줄이 나뉠 수 없음을 의미.
        pageNavigation+="&nbsp;"

        #Next 버튼(링크)
        self.cursor.execute(
            "SELECT count(*) FROM DIARY WHERE DIARY_ID < {0}".format(diary_id)
        )
        row=self.cursor.fetchone()

        if row:
            nextRowCount=row[0]
            if nextRowCount>0:
                pageNavigation+="<a href='nav:{0}'>Next</a>".format(page+1)

        pageNavigation+="</p>"
        body+=pageNavigation
        
        #html로 디스플레이 하기 위해서.
        self.outputHtmlWnd.SetPage(html.format(body),"")

    def OnNavigating(self,event):
        #event.URL이 "del:"로 시작하면 DELETE.
        if event.URL.startswith("del:")==True:
            #:오른쪽에 모든 것을 매개변수로.
            diary_id=event.URL.rpartition(":")[-1]
            self.cursor.execute(
                "DELETE FROM DIARY WHERE DIARY_ID={0}".format(diary_id)
            )
            self.cursor.execute(
                "DELETE FROM DIARY_IMG WHERE DIARY_ID={0}".format(diary_id)
            )
            self.conn.commit()
            self.LoadDiary(0)
            wx.MessageBox("삭제했습니다.", "140자 일기장", wx.OK)
        
        #event.URL이 "nav:"로 시작하면 뒤에 페이지 번호를 떼어 매개변수로 넘김.
        elif event.URL.startswith("nav:")==True:
            page=event.URL.rpartition(":")[-1]
            self.LoadDiary(int(page))
        #WebView위젯이 해당 이벤트를 받아서 해당 URL로 이동하려는 것을 방지.
        event.Skip(False)
    

if __name__=="__main__":
    app=wx.App()
    frame=MainFrame()
    frame.Show()

    app.MainLoop()