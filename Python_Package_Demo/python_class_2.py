class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi {self.name}! how are you?')


san = Person('Sangita')
san.talk()


sid = Person('Siddharth')
sid.talk()
