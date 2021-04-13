class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)

lion = Animal('lion')
lion.show()