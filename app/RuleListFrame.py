from tkinter import *
from tkinter import ttk

from app.RuleList import *

'''
This class is used to display the list of Rules that the user can click on to select and apply a Rule
which fills the rename frame inputs with the Rule attributes' values
'''


class RuleListFrame:
    def __init__(self, master, rename_frame):
        '''
        Loads the Rule list from the .ini file
        Loops over the Rule list to display the Rule names as radio buttons that the user can then select
        '''
        self.master = master
        self.rename_frame = rename_frame

        self.prompt_label = Label(self.master, text = 'Choisissez une règle à appliquer :')
        self.prompt_label.place(x = 50, y = 10)

        self.rule_list = RuleList([])
        self.rule_list.load('FTFY.ini')

        self.rules = self.rule_list.get_rules()
        self.radio_var = IntVar()
        i = 0
        j = 40

        for rule in self.rules:
            ttk.Radiobutton(self.master, text = rule.get_rule_name(), variable = self.radio_var, value = i).place(x = 50, y = j)
            i += 1
            j += 20

        self.apply_button = Button(self.master, text = 'Appliquer', command = self.apply)
        self.apply_button.place(relx = 0.25, rely = 0.9)

        self.close_button = Button(self.master, text = 'Annuler', command = self.close)
        self.close_button.place(relx = 0.5, rely = 0.9)

    def apply(self):
        '''
        Retrieves the Rule using the selected radio button value
        Clears the rename frame form (I guess I could have used the clear_form() function but whatever)
        Sets the rename frame inputs with the Rule attributes' values
        Closes the window
        '''
        rule = self.rules[self.radio_var.get()]
        MAPPING = {'' : 'Aucune', 'letter' : 'Lettre', 'number' : 'Chiffre'}
        self.rename_frame.combo_var.set(MAPPING[rule.get_initiation()])
        self.rename_frame.from_init_entry.delete(0, END)
        self.rename_frame.from_init_entry.insert(0, rule.get_from_init())
        self.rename_frame.prefix_entry.delete(0, END)
        self.rename_frame.prefix_entry.insert(0, rule.get_prefix())

        if isinstance(rule.get_file_name(), str):
            self.rename_frame.radio_var.set('rename')
            self.rename_frame.file_name_entry.delete(0, END)
            self.rename_frame.file_name_entry.insert(0, rule.get_file_name())
        else:
            self.rename_frame.radio_var.set('original')
            self.rename_frame.file_name_entry.delete(0, END)

        self.rename_frame.suffix_entry.delete(0, END)
        self.rename_frame.suffix_entry.insert(0, rule.get_suffix())

        string = ''
        i = 1
        for e in rule.get_extension():
            string += e
            if i < len(rule.get_extension()):
                string += ','
            i += 1
        self.rename_frame.extension_entry.delete(0, END)
        self.rename_frame.extension_entry.insert(0, string)

        self.master.destroy()

    def close(self):
        '''
        Closes the window
        '''
        self.master.destroy()