import unittest
from app.RuleList import *
from app.Rule import *


class RuleListTest(unittest.TestCase):
    def test_save_all(self):
        rule1 = Rule('letter', 'AA', '_', True, '_', ['.jpg', '.png'], 'Test')
        rule2 = Rule('', '', '', 'test', '', [])
        rule_list = RuleList([rule1, rule2])
        rule_list.save_all('test.ini')
        with open('test.ini', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [x.strip() for x in lines]
        self.assertEqual('letter,AA,_,True,_,Test/.jpg,.png', lines[0])
        self.assertEqual(',,,test,,/', lines[1])

    def test_load(self):
        rule_list1 = RuleList([])
        rule_list1.load('test.ini')
        rule1 = Rule('letter', 'AA', '_', True, '_', ['.jpg', '.png'], 'Test')
        rule2 = Rule('', '', '', 'test', '', [])
        rule_list2 = RuleList([rule1, rule2])
        self.assertEqual(rule_list2.__str__(), rule_list1.__str__())


if __name__ == '__main__':
    unittest.main()
