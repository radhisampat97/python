## super() with Multiple Inheritance

class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)

class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonWingedMammal, NonMarineMammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')

d = Dog()
print(' ')
bat = NonMarineMammal('Bat')
