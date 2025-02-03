class IOstring:
    def __init__(self):
        self.name="" 
    def get_name(self):
        self .name=input("what is your name:       ")
    def print_name(self):
        print("The Name Is!!!:  ", self.name.upper() )
obj=IOstring()
obj.get_name()
obj.print_name()