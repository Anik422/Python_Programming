class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("Eat")
# Animal : Parent, Base class
# Mammal : child, sub class
class Mammal(Animal):
    def walk(self):
        print("Walk")





n = Mammal()
n.eat()
n.walk()
print(n.age)
print(isinstance(n, object))
print(issubclass(Mammal, Animal))