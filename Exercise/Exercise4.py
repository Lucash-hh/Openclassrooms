class InputOutString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Input string: ")

    def print_string(self):
        print(self.s.upper())

str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()