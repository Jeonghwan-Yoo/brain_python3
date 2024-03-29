import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Panel Example")
        self.panel=wx.Panel(self)
        self.panel.SetBackgroundColour(wx.RED)

        self.button1=wx.Button(self.panel, label="(50,50)") #self.panel위에 생성
        #self.panel의 좌상단으로부터 50,50떨어진 곳에 위치
        self.button1.SetPosition((50,50))

        self.button2=wx.Button(self.panel, label="(250,100)")
        #self.panel의 좌상단으로부터 250,100떨어진 곳에 위치
        self.button2.SetPosition((250,100))

if __name__=="__main__":
    app=wx.App()
    frame=MyFrame()
    frame.Show()

    app.MainLoop()
