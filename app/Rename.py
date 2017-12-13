import os

from app.Action import *

'''
This class is used to rename the files on the system
'''


class Rename(Action):
    def __init__(self, directory_name, rule):
        Action.__init__(self, directory_name, rule)

    def rename_files(self):
        '''
        Retrieves the tuple returned by simulation()
        Loops over the lists and renames the files
        Returns the number of files renamed
        '''
        original, renamed = self.simulation()
        j = 0
        for i in range(len(original)):
            os.rename(os.path.join(self.directory_name, original[i]),
                      os.path.join(self.directory_name, renamed[i]))
            j += 1
        return j
