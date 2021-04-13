class animal:
    def __init__(self, name):
        self.name = name
    def showName(self):
        print(self.name)

lion = animal('lion')
lion.showName()