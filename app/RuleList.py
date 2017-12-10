from app.Rule import *


class RuleList:
    def __init__(self, rules):
        self.rules = rules

    def get_rules(self):
        return self.rules

    def set_rules(self, rules):
        self.rules = rules

    def __str__(self):
        string = ''
        for r in self.rules:
            string += r.__str__() + '\n \n'
        return string

    def save_all(self, file_name):
        with open(file_name, 'w', encoding = 'utf-8') as file:
            string = ''
            for r in self.rules:
                string += r.get_initiation() + ',' + r.get_from_init() + ',' + r.get_prefix() + ',' + \
                          str(r.get_file_name()) + ',' + r.get_suffix() + ',' + r.get_rule_name() + '/'
                i = 1
                for e in r.get_extension():
                    string += e
                    if i < len(r.get_extension()):
                        string += ','
                    i += 1
                string += '\n'
            file.write(string)

    def save(self, file_name, rule):
        with open(file_name, 'a', encoding='utf-8') as file:
            string = rule.get_initiation() + ',' + rule.get_from_init() + ',' + rule.get_prefix() + ',' + \
                      str(rule.get_file_name()) + ',' + rule.get_suffix() + ',' + rule.get_rule_name() + '/'
            i = 1
            for e in rule.get_extension():
                string += e
                if i < len(rule.get_extension()):
                    string += ','
                i += 1
            string += '\n'
            file.write(string)

    def load(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [x.strip() for x in lines]
        for line in lines:
            split = line.split('/')
            file_name_attributes = split[0].split(',')
            extension = split[1].split(',')

            if file_name_attributes[3] == 'True':
                file_name_attributes[3] = True
            elif file_name_attributes[3] == 'False':
                file_name_attributes[3] = False

            rule = Rule(file_name_attributes[0], file_name_attributes[1], file_name_attributes[2],
                        file_name_attributes[3], file_name_attributes[4], extension, file_name_attributes[5])

            self.rules.append(rule)

    def add_rule(self, file_name, rule):
        self.rules.append(rule)
        self.save(file_name, rule)