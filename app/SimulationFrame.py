from tkinter import *
from tkinter import messagebox

'''
This class is used to display the renaming simulation of the files and actually rename them
'''


class SimulationFrame:
    def __init__(self, master, rename_action, rename_frame):
        self.master = master
        self.rename_action = rename_action
        self.rename_frame = rename_frame

        self.prompt_label = Label(self.master, text = 'Etes-vous sûr de vouloir renommer ces fichiers ?')
        self.prompt_label.place(x = 50, y = 10)

        self.original, self.renamed = self.rename_action.simulation()
        j = 40
        for i in range(len(self.original)):
            Label(self.master, text = self.original[i] + ' -> ' + self.renamed[i]).place(x = 50, y = j)
            j += 20

        self.rename_button = Button(self.master, text = 'Oui', command = self.rename)
        self.rename_button.place(relx = 0.4, rely = 0.9)

        self.close_button = Button(self.master, text = 'Non', command = self.close)
        self.close_button.place(relx = 0.5, rely = 0.9)

    def rename(self):
        '''
        Checks if multiple file names are the same
        If it is the case a popup is triggered to inform the user and to prevent a system error
        Otherwise the files are renamed and a popup with the number of files renamed is triggered
        Closes the window and clears the rename frame form
        '''
        seen = set()
        duplicates = set(x for x in self.renamed if x in seen or seen.add(x))
        if len(duplicates) == 0:
            nb_files = self.rename_action.rename_files()
            self.master.destroy()
            messagebox.showinfo('Fichiers renommés', 'Nombre de fichiers renommés : ' + str(nb_files))
            self.rename_frame.clear_form()
        else:
            messagebox.showinfo('Avertissement', 'Opération impossible : \n'
                                                 'Un ou plusieurs fichiers ont le même nom et la même extension')

    def close(self):
        '''
        Closes the window
        '''
        self.master.destroy()