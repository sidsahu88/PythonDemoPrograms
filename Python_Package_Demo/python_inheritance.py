# Parent Class
class Mammal:
    def walk(self):
        print('Walking...')

class Fish:
    def swim(self):
        print('Swimming...')

# Child Class
class Dog(Mammal):
    pass  # To not defining any method of class

class Cat(Mammal):
    def jump(self):
        print('Jumping...')

class Whale(Mammal, Fish):
    def walk(self):
        raise NotImplementedError("Whale cannot walk!")


dog = Dog()
print('Dog: ')
dog.walk()

cat = Cat()
print('\nCat')
cat.walk()
cat.jump()


w = Whale()
print('\nWhale')
w.swim()
w.walk()
