import unittest
from app.Action import *
from app.Rule import *


class ActionTest(unittest.TestCase):
    '''
    /!\ A lire
    Je passe en français pour bien expliquer
    Ce test va fail car simulation() retourne une liste vide à chaque fois
    alors que ma méthode fonctionne bien dans l'application
    et fonctionnait aussi dans un main de test avant que je crée les niveaux 'app' et 'test'
    J'ai testé avec plusieurs répertoires et simulation() retourne une liste vide ici
    alors qu'elle retourne ce qui est attendu dans l'application
    J'ai essayé de mettre la classe de test au même niveau que la classe Action sans succès
    Je ne vois pas d'où vient l'erreur même après avoir débuggé (peut-être l'import os qui plante)
    J'écris donc ce test qui est censé passer
    '''
    def test_simulation(self):
        rule1 = Rule('', '', '', True, '', [])
        rule2 = Rule('letter', 'AA', '_', 'Toto', '_', ['.jpg', '.png'])
        rule3 = Rule('number', '', 'x', 'RENAMED', 'x', ['.txt', '.jpg', '.none'])
        action = Action('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', rule1)
        expected_original = ['test.jpg', 'test.png', 'test.txt']
        expected_renamed = ['test.jpg', 'test.png', 'test.txt']
        actual_original, actual_renamed = action.simulation()
        self.assertEqual(expected_original, actual_original)
        self.assertEqual(expected_renamed, actual_renamed)
        action = Action('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', rule2)
        expected_renamed = ['AB_Toto_.jpg', 'AC_Toto_.png']
        actual_original, actual_renamed = action.simulation()
        self.assertEqual(expected_original, actual_original)
        self.assertEqual(expected_renamed, actual_renamed)
        action = Action('D:\Projets\Projets PyCharm\FTFY\\test\Test Directory', rule3)
        expected_renamed = ['001xRENAMEDx.jpg', '002xRENAMEDx.txt']
        actual_original, actual_renamed = action.simulation()
        self.assertEqual(expected_original, actual_original)
        self.assertEqual(expected_renamed, actual_renamed)


if __name__ == '__main__':
    unittest.main()
