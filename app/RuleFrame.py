from tkinter import messagebox

from app.FrameTemplate import *
from app.RuleList import *

'''
This class is used to display the rule frame from which you can create and persist a Rule
It extends FrameTemplate and adds the specific labels and button
'''


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
        '''
        Retrieves the Rule created from the user inputs
        Sets the Rule name retrieved from the name_entry
        Instantiates an empty RuleList
        Adds the Rule to the RuleList which also persists the Rule in the .ini file
        Closes the window and triggers a popup
        '''
        rule = self.get_rule()
        rule.set_rule_name(self.name_entry.get())
        rule_list = RuleList([])
        rule_list.add_rule('FTFY.ini', rule)
        self.master.destroy()
        messagebox.showinfo('Règle enregistrée', 'Règle enregistrée')