I had to add the following code to make the .exe work with bundled logo.png :

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


I use this function when 'logo.png' is called

This is not in the sources because I had to tweak a few things to create the .exe app (reorganize the project, refactor code, etc) which broke some tests and maybe some code.

I don't have time to check if everything is working correctly and I don't want to take any chances so I'll leave it at that