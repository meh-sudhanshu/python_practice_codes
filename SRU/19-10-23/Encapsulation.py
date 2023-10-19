class Encapsulation:
    def __init__(self):
        self.name = "Sudhanshu Kumar"
        self.age = "25"
    def get_name(self):
        print(self.name)
    def set_name(self,value):
        self.name = value

obj = Encapsulation()
obj.get_name()