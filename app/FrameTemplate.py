from tkinter import *
from tkinter import ttk

from app.Rule import *


class FrameTemplate:
    def __init__(self, master):
        self.master = master
        self.name_entry = Entry(self.master)
        self.name_entry.configure(width = 40)
        self.name_entry.place(x = 150, y = 55)

        self.initiation_label = Label(self.master, text = 'Amorce')
        self.initiation_label.place(x = 35, y = 125)
        self.combo_var = StringVar()
        self.combo_var.set('Aucune')
        self.initiation_box = ttk.Combobox(self.master, textvariable = self.combo_var, state = 'readonly', values = ['Aucune', 'Lettre', 'Chiffre'])
        self.initiation_box.configure(width = 8)
        self.initiation_box.place(x = 25, y = 150)
        self.MAPPING = {'Aucune' : '', 'Lettre' : 'letter', 'Chiffre' : 'number'}

        self.from_init_label = Label(self.master, text = 'A partir de')
        self.from_init_label.place(x = 27, y = 225)
        self.from_init_entry = Entry(self.master)
        self.from_init_entry.configure(width = 9)
        self.from_init_entry.place(x = 27, y = 250)

        self.prefix_label = Label(self.master, text = 'Préfixe')
        self.prefix_label.place(x = 140, y = 125)
        self.prefix_entry = Entry(self.master)
        self.prefix_entry.configure(width = 10)
        self.prefix_entry.place(x = 129, y = 150)

        self.file_name_label = Label(self.master, text = 'Nom du fichier')
        self.file_name_label.place(x = 225, y = 125)
        self.radio_var = StringVar()
        self.radio_var.set('original')
        self.file_name_rb1 = ttk.Radiobutton(self.master, text = 'Nom original', variable = self.radio_var, value = 'original')
        self.file_name_rb2 = ttk.Radiobutton(self.master, variable = self.radio_var, value = 'rename')
        self.file_name_rb1.place(x = 215, y = 150)
        self.file_name_rb2.place(x = 215, y = 180)
        self.file_name_entry = Entry(self.master)
        self.file_name_entry.configure(width = 12)
        self.file_name_entry.place(x = 235, y = 180)

        self.suffix_label = Label(self.master, text = 'Postfixe')
        self.suffix_label.place(x = 350, y = 125)
        self.suffix_entry = Entry(self.master)
        self.suffix_entry.configure(width = 10)
        self.suffix_entry.place(x = 342, y = 150)

        self.extension_label = Label(self.master, text = 'Extension(s) concernée(s)')
        self.extension_label.place(x = 440, y = 125)
        self.extension_entry = Entry(self.master)
        self.extension_entry.configure(width = 20)
        self.extension_entry.place(x = 447, y = 150)

        self.image = PhotoImage(file = 'logo.png')
        self.image_label = Label(self.master, image = self.image)
        self.image_label.place(x = 450, y = 20)

    def get_rule(self):
        initiation = self.MAPPING[self.initiation_box.get()]
        from_init = self.from_init_entry.get()
        prefix = self.prefix_entry.get()

        if self.radio_var.get() == 'original':
            file_name = True
        else:
            file_name = self.file_name_entry.get()

        suffix = self.suffix_entry.get()
        extension = self.extension_entry.get().split(',')

        return Rule(initiation, from_init, prefix, file_name, suffix, extension)

    def clear_form(self):
        self.name_entry.delete(0, END)
        self.combo_var.set('Aucune')
        self.from_init_entry.delete(0, END)
        self.prefix_entry.delete(0, END)
        self.radio_var.set('original')
        self.file_name_entry.delete(0, END)
        self.suffix_entry.delete(0, END)
        self.extension_entry.delete(0, END)
        self.name_entry.focus_set()