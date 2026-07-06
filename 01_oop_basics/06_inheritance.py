class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def bark(self):
        return "Woo!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

class Pet(Dog, Cat):
    def info(self):
        return "This is a pet animal"

pet = Pet()
print(pet.speak())
print(pet.bark())
print(pet.meow())
print(pet.info())


class Animal2:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some generic animal sound"

class Dog2(Animal2):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        return "Woof!"

dog = Dog2("Buddy", "Golden Retriever")
print(dog.name)
print(dog.breed)
print(dog.speak())
