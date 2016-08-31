import wx
import time

class MainFrame(wx.Frame):
           
    def __init__(self):
        
        wx.Frame.__init__(self, None, title='Nonsense App') 
        
        self.make_menu()

        panel = wx.Panel(self,size=(350,300))
        panel.SetBackgroundColour(wx.BLACK)

        text_box = wx.TextCtrl(panel, size=(150,200), pos=(10,10), style=wx.TE_MULTILINE)

        abort_btn = wx.Button(panel, label='ABORT!', size=(100,40), pos=(200,150))
        abort_btn.SetBackgroundColour('Red')
        abort_btn.Bind(wx.EVT_BUTTON, self.abort)

        time_btn = wx.Button(panel, label='GET \nLONDON \nTIME', size=(100,100), pos=(200,20))
        time_btn.SetBackgroundColour(wx.GREEN)
        time_btn.Bind(wx.EVT_BUTTON, self.get_time)

        self.SetMinSize((350, 300))
        self.SetMaxSize((350, 300))
        self.CreateStatusBar()

        self.SetSize((350, 300))
        self.SetTitle('Nonsense App')
        self.Centre()
        self.Show(True)          
        
    def make_menu(self):
        
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        editmenu = wx.Menu()
        helpmenu = wx.Menu()
        
        filemenu.Append(wx.ID_ANY, 'Quit', 'Quit application')
        editmenu.Append(wx.ID_ANY, 'Paste', 'Paste')
        helpmenu.Append(wx.ID_ANY, 'About', 'About')

        menubar.Append(filemenu, 'File')
        menubar.Append(editmenu, 'Edit')
        menubar.Append(helpmenu, 'Help')

        self.SetMenuBar(menubar)   

    def abort(self,event):
    	msg = wx.MessageDialog(None, 'Mission Aborted!', 'Too Late', wx.OK)
    	msg.ShowModal()

    def get_time(self, event):
    	the_time = time.gmtime()
    	time_string = ('Current time in London is ' + str(the_time.tm_hour) +
    					':' + str(the_time.tm_min))
    	msg = wx.MessageDialog(None, time_string, 'Time', wx.OK )
    	msg.ShowModal()

                      
def main():
    
    app = wx.App()
    MainFrame()
    app.MainLoop()    

main()          