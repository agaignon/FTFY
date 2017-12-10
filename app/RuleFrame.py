from tkinter import messagebox

from app.FrameTemplate import *
from app.RuleList import *


class RuleFrame(FrameTemplate):
    def __init__(self, master):
        FrameTemplate.__init__(self, master)

        self.title_label = Label(self.master, text = 'Créer une règle')
        self.title_label.place(x = 225, y = 15)

        self.name_label = Label(self.master, text = 'Nom de la règle')
        self.name_label.place(x = 55, y = 53)

        self.create_button = Button(self.master, text = 'Créer', command = self.create)
        self.create_button.place(x = 450, y = 225)

    def create(self):
        rule = self.get_rule()
        rule.set_rule_name(self.name_entry.get())
        rule_list = RuleList([])
        rule_list.add_rule('FTFY.ini', rule)
        self.master.destroy()
        messagebox.showinfo('Règle enregistrée', 'Règle enregistrée')