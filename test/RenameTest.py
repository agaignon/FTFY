import unittest
from app.Rename import *
from app.Rule import *


class RenameTest(unittest.TestCase):
    def test_rename_files(self):
        '''
        /!\ A lire
        Idem que pour ActionTest::test_simulation()
        rename_files() utilise l'output de simulation() et je ne peux pas renommer à partir d'une liste vide
        '''
        rule1 = Rule('', '', '', True, '', [])
        rule2 = Rule('letter', 'AA', '_', 'Toto', '_', ['.jpg', '.png'])
        rule3 = Rule('number', '', 'x', 'RENAMED', 'x', ['.txt', '.jpg', '.none'])
        rename_action = Rename('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', rule1)
        nb_renamed_files = rename_action.rename_files()
        expected_renamed = ['test.jpg', 'test.png', 'test.txt']
        actual_renamed = [fn for fn in os.listdir(rename_action.get_directory_name())]
        self.assertEqual(3, nb_renamed_files)
        self.assertEqual(expected_renamed, actual_renamed)
        rename_action = Rename('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', rule2)
        nb_renamed_files = rename_action.rename_files()
        expected_renamed = ['AB_Toto_.jpg', 'AC_Toto_.png', 'test.txt']
        actual_renamed = [fn for fn in os.listdir(rename_action.get_directory_name())]
        self.assertEqual(2, nb_renamed_files)
        self.assertEqual(expected_renamed, actual_renamed)
        rename_action = Rename('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', rule3)
        nb_renamed_files = rename_action.rename_files()
        expected_renamed = ['001xRENAMEDx.jpg', '002xRENAMEDx.txt', 'AC_Toto_.png']
        actual_renamed = [fn for fn in os.listdir(rename_action.get_directory_name())]
        self.assertEqual(2, nb_renamed_files)
        self.assertEqual(expected_renamed, actual_renamed)
        reset_rule = Rule('', '', '', 'test', '', [])
        rename_action = Rename('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', reset_rule)
        rename_action.rename_files()