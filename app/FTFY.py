import tkinter as tk

from app.MainApplication import *

'''
App launcher
'''


def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()
