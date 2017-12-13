from app.RenameFrame import *
from app.Toolbar import *

'''
Controller of the app
'''


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title('FTFY')
        self.master.resizable(width = False, height = False)
        self.master.minsize(width = 600, height = 300)
        self.rename_frame = RenameFrame(self.master)
        self.toolbar = Toolbar(self.master, self.rename_frame)