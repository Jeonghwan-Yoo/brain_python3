import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Menu Example")
        
        self.menuBar=wx.MenuBar()
        fileMenu=wx.Menu()
        fileNewMenu=fileMenu.Append(wx.ID_ANY, "새 파일")
        fileOpenMenu=fileMenu.Append(wx.ID_ANY,"열기")
        fileMenu.AppendSeparator() #메뉴항목이 들어갈 자리에 가로선을 추가.
        fileExitMenu=fileMenu.Append(wx.ID_ANY,"끝내기")

        customMenu=wx.Menu()
        customHelloMenu=customMenu.Append(wx.ID_ANY,"&Hello")
        #&는 뒤따라오는 알파벳에 밑줄을 긋고 Alt키를 이용해 메뉴항목을 실행할 수 있게 함.
        self.menuBar.Append(fileMenu,"&File")
        self.menuBar.Append(customMenu,"&Test")
        self.SetMenuBar(self.menuBar)
        
        #각 메뉴 항목에 대해 EVT_MENU와 이벤트 처리기를 연결합니다.
        self.Bind(wx.EVT_MENU, self.OnNew, fileNewMenu)
        self.Bind(wx.EVT_MENU, self.OnOpen, fileOpenMenu)
        self.Bind(wx.EVT_MENU, self.OnExit, fileExitMenu)
        self.Bind(wx.EVT_MENU, self.OnHello, customHelloMenu)

    def OnNew(self, e):
        wx.MessageBox("OnNew() Clicked!")

    def OnOpen(self, e):
        wx.MessageBox("OnOpen() Clicked!")
    
    def OnExit(self, e):
        self.Close()

    def OnHello(self, e):
        wx.MessageBox("Hello.")

if __name__=="__main__":
    app=wx.App()
    frame=MyFrame()
    frame.Show()

    app.MainLoop()