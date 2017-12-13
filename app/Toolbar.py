from app.RuleFrame import *
from app.RuleListFrame import *

'''
This class is used to display the toolbar from which the user can open the rule and rule list frames
The user can also get some info about the software
'''


class Toolbar:
    def __init__(self, master, rename_frame):
        self.master = master
        self.rename_frame = rename_frame

        self.menu_bar = Menu(self.master)
        self.rule_menu = Menu(self.menu_bar, tearoff = 0)
        self.rule_menu.add_command(label = 'Lister', command = self.open_rule_list_frame)
        self.rule_menu.add_command(label = 'Créer', command = self.open_rule_frame)
        self.menu_bar.add_cascade(label = 'Règles', menu = self.rule_menu)
        self.menu_bar.add_command(label = '?', command = self.open_about)

        self.master.config(menu = self.menu_bar)

    def open_rule_list_frame(self):
        '''
        Opens the rule list frame
        '''
        self.new_window_rl = Toplevel(self.master)
        self.new_window_rl.title('Liste des règles')
        self.new_window_rl.minsize(width = 300, height = 300)
        self.rule_list_frame = RuleListFrame(self.new_window_rl, self.rename_frame)

    def open_rule_frame(self):
        '''
        Opens the rule frame
        '''
        self.new_window_r = Toplevel(self.master)
        self.new_window_r.title('Créer une règle')
        self.new_window_r.resizable(width = False, height = False)
        self.new_window_r.minsize(width = 600, height = 300)
        self.rule_frame = RuleFrame(self.new_window_r)

    def open_about(self):
        '''
        Displays the software info
        '''
        messagebox.showinfo('A propos', "FTFY version 1.0 \n\n"
                                        "Logiciel développé par Augustin Gaignon \n\n"
                                        "FTFY veut dire 'Fixed That For You' qui se traduit par "
                                        "'J'ai rectifié ça pour toi' qui représente bien le but de ce logiciel")