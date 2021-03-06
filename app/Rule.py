'''
This class is used to encapsulate the different data inputs of the interfaces' forms
'''


class Rule:
    def __init__(self, initiation, from_init, prefix, file_name, suffix, extension, rule_name = ''):
        '''
        Extension list is stripped to clean the data in case the user inputs spaces
        '''
        self.initiation = initiation
        self.from_init = from_init
        self.prefix = prefix
        self.file_name = file_name
        self.suffix = suffix
        extension = [x.strip() for x in extension]
        self.extension = extension
        self.rule_name = rule_name

    def get_initiation(self):
        return self.initiation

    def set_initiation(self, initiation):
        self.initiation = initiation

    def get_from_init(self):
        return self.from_init

    def set_from_init(self, from_init):
        self.from_init = from_init

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, file_name):
        self.file_name = file_name

    def get_suffix(self):
        return self.suffix

    def set_suffix(self, suffix):
        self.suffix = suffix

    def get_extension(self):
        return self.extension

    def set_extension(self, extension):
        self.extension = extension

    def get_rule_name(self):
        return self.rule_name

    def set_rule_name(self, rule_name):
        self.rule_name = rule_name

    def __str__(self):
        string = "Initiation : '" + self.initiation + "' \n" \
                 "From init : '" + self.from_init + "' \n" \
                 "Prefix : '" + self.prefix + "' \n" \
                 "File name : '" + str(self.file_name) + "' \n" \
                 "Suffix : '" + self.suffix + "' \n" \
                 "Rule name : '" + self.rule_name + "' \n" \
                 "Extension : '"
        i = 1
        for e in self.extension:
            string += e
            if i < len(self.extension):
                string += ', '
            i += 1
        string += "'"
        return string