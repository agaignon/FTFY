import os
import string


class Action:
    def __init__(self, directory_name, rule):
        self.directory_name = directory_name
        self.rule = rule

    def get_directory_name(self):
        return self.directory_name

    def set_directory_name(self, directory_name):
        self.directory_name = directory_name

    def get_rule(self):
        return self.rule

    def set_rule(self, rule):
        self.rule = rule

    def __str__(self):
        return "Directory name : '" + self.directory_name + "' \n" + self.rule.__str__()

    def int_to_alphabet(self, int):
        string = ""
        while int > 0:
            int, remainder = divmod(int - 1, 26)
            string = chr(65 + remainder) + string
        return string

    def alphabet_to_int(self, alphabet):
        num = 0
        for c in alphabet:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        return num

    def simulation(self):
        if self.rule.get_extension() == '':
            original_file_names = [fn for fn in os.listdir(self.directory_name)]
        else:
            original_file_names = [fn for fn in os.listdir(self.directory_name)
                                   if fn.endswith(tuple(self.rule.get_extension()))]

        renamed_file_names = []

        if self.rule.get_from_init() == '' or self.rule.get_initiation() == '':
            from_init = 0
        elif self.rule.get_initiation() == 'letter':
            from_init = self.alphabet_to_int(self.rule.get_from_init())
        elif self.rule.get_initiation() == 'number':
            number = self.rule.get_from_init()
            if number.isdigit():
                from_init = int(number)
            else:
                from_init = 0

        for original_file_name in original_file_names:
            renamed_file_name, extension = os.path.splitext(original_file_name)

            if isinstance(self.rule.get_file_name(), str):
                renamed_file_name = self.rule.get_file_name()

            if self.rule.get_prefix() != '':
                renamed_file_name = self.rule.get_prefix() + renamed_file_name

            if self.rule.get_suffix() != '':
                renamed_file_name = renamed_file_name + self.rule.get_suffix()

            from_init += 1

            if self.rule.get_initiation() == '':
                initiation = ''
            elif self.rule.get_initiation() == 'letter':
                initiation = self.int_to_alphabet(from_init)
            elif self.rule.get_initiation() == 'number':
                initiation = '{0}'.format(str(from_init).zfill(3))

            if initiation != '':
                renamed_file_name = initiation + renamed_file_name

            renamed_file_name = renamed_file_name + extension

            renamed_file_names.append(renamed_file_name)

        return original_file_names, renamed_file_names