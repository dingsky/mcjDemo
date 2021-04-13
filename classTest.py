class Animal:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)


if __name__=="__main__":
    lion = Animal('lion')
    lion.show()