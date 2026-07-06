from abc import ABC, abstractmethod

class Recipe(ABC):
    def make(self):
        self.boil()
        self.brew()
        self.pour()
        self.add_extras()

    def boil(self):
        print("  Boiling water")

    def pour(self):
        print("  Pouring into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

class Tea(Recipe):
    def brew(self):
        print("  Steeping tea leaves")

    def add_extras(self):
        print("  Adding lemon")

class Coffee(Recipe):
    def brew(self):
        print("  Dripping coffee")

    def add_extras(self):
        print("  Adding sugar and milk")


print("Making tea:")
Tea().make()

print("\nMaking coffee:")
Coffee().make()
