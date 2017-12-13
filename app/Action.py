import os
import string

'''
This class is used to simulate the renaming of files
'''


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
        '''
        Takes an int as parameter and converts it into its corresponding alphabet letter using the ASCII table
        We use the powers of 26 to know how many times we have to loop and how many characters will be in the string output
        e.g. 'Z' is 26*26^0 and 'ZZ' is 26*26^1 + 26*26^0 and so on
        We use the remainder of the integer division to know the letter we have to display
        65 is the ASCII value of 'A' and we had to subtract 1 because 'A' corresponds to 65 + 0 but in the user input 'A' is 1
        So then if we want 'B' user will input 2 so we have 2 - 1 and we get chr(65 + 1) which is 'B'
        >>> int_to_alphabet(26)
        'Z'
        >>> int_to_alphabet(52)
        'AZ'
        '''
        string = ""
        while int > 0:
            int, remainder = divmod(int - 1, 26)
            string = chr(65 + remainder) + string
        return string

    def alphabet_to_int(self, alphabet):
        '''
        Takes a string e.g. one or several alphabet letters and converts it into its corresponding int value
        We loop each character of the string and check if it is an ASCII letter
        And then we convert it into an int using the ASCII table
        ord('A') is 65 so it's a base for our conversion and we add 1 because it's zero based
        And we also put the character to upper case so it's coherent even if the user input lower case
        Note that before each sum we multiply the num by 26 to account for the powers of 26
        >>> alphabet_to_int('Z')
        26
        >>> alphabet_to_int('AZ')
        52
        '''
        num = 0
        for c in alphabet:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        return num

    def simulation(self):
        '''
        Fetches the file names contained in the given directory
        File names are filtered by extension or not depending on the user input
        from_init is initiated according to the user input
        from_init is used as a counter to create the initiation if there is one
        Then we create the renamed version for each file name depending on the user input
        Finally we return a tuple containing a list of the original file names and a list of the renamed file names
        '''
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