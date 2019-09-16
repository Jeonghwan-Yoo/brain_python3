import wx

class MyApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Window Colour")
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRButtonDown)
    def OnMouseLButtonDown(self, event):
        self.SetBackgroundColour(wx.Colour(0,0,255,0))
        #즉시 배경색이 바뀌지 않을 수 있으니 wx.Frame객체가 배경을 다시 그리도록합니다.
        self.Refresh()

    def OnMouseRButtonDown(self, event):
        self.SetBackgroundColour(wx.Colour(255,0,0,0))
        self.Refresh()

if __name__=='__main__':
    app=wx.App()
    frame=MyApp()
    frame.Show()

    app.MainLoop()