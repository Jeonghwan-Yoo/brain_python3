import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="FlexGridSizer Example")
        self.SetSize(300,170)
        self.mainPanel=wx.Panel(self)

        self.fgridSizer=wx.FlexGridSizer(rows=3, cols=2, hgap=5, vgap=5)
        
        self.staticName=wx.StaticText(self.mainPanel, label="Name:")
        self.staticEmail=wx.StaticText(self.mainPanel, label="Email:")
        self.staticPhone=wx.StaticText(self.mainPanel, label="Phone:")
        
        self.textName=wx.TextCtrl(self.mainPanel)
        self.textEmail=wx.TextCtrl(self.mainPanel)
        self.textPhone=wx.TextCtrl(self.mainPanel)

        self.fgridSizer.Add(self.staticName)
        self.fgridSizer.Add(self.textName,0,wx.EXPAND)
        self.fgridSizer.Add(self.staticEmail)
        self.fgridSizer.Add(self.textEmail,0,wx.EXPAND)
        self.fgridSizer.Add(self.staticPhone)
        self.fgridSizer.Add(self.textPhone,0,wx.EXPAND)

        #윈도우 크기 변경시 두 번째 열의 너비도 따라 변경되도록 지정
        self.fgridSizer.AddGrowableCol(1)

        #윈도우 크기 변경시 세 번째 행의 높이도 따라 변경되도록 지정
        self.fgridSizer.AddGrowableRow(2)

        self.vtBoxSizer=wx.BoxSizer(wx.VERTICAL) #위/아래
        self.vtBoxSizer.Add(self.fgridSizer,1,wx.EXPAND|wx.ALL, 5)
        self.mainPanel.SetSizer(self.vtBoxSizer)

if __name__=="__main__":
    app=wx.App()
    frame=MyFrame()
    frame.Show()

    app.MainLoop()