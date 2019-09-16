import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Close Event")
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        if wx.MessageBox("윈도우를 닫을까요?","확인",wx.YES_NO) != wx.YES:
            #Event.Skip()메소드는 현재의 이벤트 처리기를 거친 후에도 계속 처리할 것인지를 지정
            #True면 다음 이벤트 처리기로 넘어감.
            #True였다면 띄운 창도 닫힐 것입니다.
            #False를 입력해 해당 이벤트를 추가로 처리하지 않게 만듭니다.
            event.Skip(False)
        else:
            self.Destroy()

if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    
    app.MainLoop()