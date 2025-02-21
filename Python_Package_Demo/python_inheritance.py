# Parent Class
class Mammal:
    def walk(self):
        print('Walk')


class Dog(Mammal):
    pass  # To not defining any method of class


class Cat(Mammal):
    def jump(self):
        print('Jump')


dog = Dog()
print('Dog: ')
dog.walk()

cat = Cat()
print('\nCat')
cat.walk()
cat.jump()
