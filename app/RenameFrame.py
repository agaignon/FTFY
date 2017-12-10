from app.FrameTemplate import *
from app.Rename import *
from app.SimulationFrame import *


class RenameFrame(FrameTemplate):
    def __init__(self, master):
        FrameTemplate.__init__(self, master)

        self.title_label = Label(self.master, text = 'Renommer en lots')
        self.title_label.place(x = 225, y = 15)

        self.name_label = Label(self.master, text = 'Chemin du répertoire')
        self.name_label.place(x = 25, y = 53)

        self.rename_button = Button(self.master, text = 'Renommer', command = self.rename)
        self.rename_button.place(x = 450, y = 225)

    def rename(self):
        directory_name = self.name_entry.get()
        if os.path.isdir(directory_name):
            rule = self.get_rule()
            rename_action = Rename(directory_name, rule)
            self.new_window = Toplevel(self.master)
            self.new_window.title('Prévisualisation')
            self.new_window.minsize(width = 375, height = 300)
            self.simulation_frame = SimulationFrame(self.new_window, rename_action, self)
        else:
            messagebox.showinfo('Info', "Le répertoire donné n'existe pas")