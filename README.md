# SDLP — Extracted Codes from Materials

## 01 — OOP Basics

### 01_classes_objects.py
```python
class Student:
    name = "Tanvir Ahmed"
    roll = "10101"

s1 = Student()
print("Name:", s1.name)
print("Roll:", s1.roll)
```

### 02_constructor.py
```python
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

s1 = Student("Tony Stark", 3.55)
s2 = Student("Iron Man", 2.22)

print(s1.name, s1.cgpa)
print(s2.name, s2.cgpa)
```

### 03_class_vs_instance.py
```python
class Student:
    uni_name = "NITER"

s1 = Student()
print("Via instance:", s1.uni_name)
print("Via class:   ", Student.uni_name)
```

### 04_methods.py
```python
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def good_morning(self):
        return self.name

s1 = Student("Tony Stark", 3.55)
print(s1.good_morning())
```

### 05_static_method.py
```python
class MyClass:
    @staticmethod
    def my_static_method():
        print("Hi! Static method called.")

MyClass.my_static_method()
```

### 06_inheritance.py
```python
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
```

### 07_abstraction.py
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
```

### 08_encapsulation.py
```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("John", 25)
print(person.get_name())

person.set_name("Alice")
print(person.get_name())
```

## 02 — Factory Pattern

### 01_shape_factory.py
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing Circle"

class Square(Shape):
    def draw(self):
        return "Drawing Square"

class Rectangle(Shape):
    def draw(self):
        return "Drawing Rectangle"

class ShapeFactory:
    @staticmethod
    def get_shape(type_):
        if type_ == "circle":
            return Circle()
        if type_ == "square":
            return Square()
        if type_ == "rectangle":
            return Rectangle()
        return None


factory = ShapeFactory()

s1 = factory.get_shape("circle")
print(s1.draw())

s2 = factory.get_shape("square")
print(s2.draw())

s3 = factory.get_shape("rectangle")
print(s3.draw())
```

## 03 — Abstract Factory Pattern

### 01_gui_factory.py
```python
from abc import ABC, abstractmethod

# Abstract products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass

# Light theme products
class LightButton(Button):
    def render(self):
        return "Light Button"

class LightTextBox(TextBox):
    def render(self):
        return "Light TextBox"

# Dark theme products
class DarkButton(Button):
    def render(self):
        return "Dark Button"

class DarkTextBox(TextBox):
    def render(self):
        return "Dark TextBox"

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass

# Concrete factories
class LightFactory(GUIFactory):
    def create_button(self):
        return LightButton()

    def create_textbox(self):
        return LightTextBox()

class DarkFactory(GUIFactory):
    def create_button(self):
        return DarkButton()

    def create_textbox(self):
        return DarkTextBox()


def show_theme(factory):
    btn = factory.create_button()
    txt = factory.create_textbox()
    print(btn.render())
    print(txt.render())


show_theme(LightFactory())
print("---")
show_theme(DarkFactory())
```

## 04 — Builder Pattern

### 01_burger_builder.py
```python
class Burger:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def __str__(self):
        return (f"Burger(size={self.size}, cheese={self.cheese}, "
                f"pepperoni={self.pepperoni}, lettuce={self.lettuce}, "
                f"tomato={self.tomato})")

class BurgerBuilder:
    def __init__(self, size):
        self.burger = Burger()
        self.burger.size = size

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_pepperoni(self):
        self.burger.pepperoni = True
        return self

    def add_lettuce(self):
        self.burger.lettuce = True
        return self

    def add_tomato(self):
        self.burger.tomato = True
        return self

    def build(self):
        return self.burger


b = BurgerBuilder("Large").add_cheese().add_pepperoni().add_tomato().build()
print(b)
```

## 06 — Adapter Pattern

### 01_adapter.py
```python
class USBCCharger:
    def charge(self):
        return "Charging via USB-C"

class USBBPort:
    def connect(self):
        return "Connected to USB-B port"

class Adapter(USBCCharger):
    def __init__(self, port):
        self.port = port

    def charge(self):
        return self.port.connect() + " using USB-C to USB-B adapter"


phone = USBBPort()
charger = Adapter(phone)
print(charger.charge())
```

## 07 — Composite Pattern

### 01_file_system.py
```python
from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def show(self, indent=""):
        pass

class File(FileSystem):
    def __init__(self, name):
        self.name = name

    def show(self, indent=""):
        print(f"{indent}File: {self.name}")

class Folder(FileSystem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def show(self, indent=""):
        print(f"{indent}Folder: {self.name}")
        for child in self.children:
            child.show(indent + "  ")


f1 = File("readme.txt")
f2 = File("photo.jpg")
f3 = File("data.csv")

sub = Folder("Documents")
sub.add(f1)
sub.add(f2)

root = Folder("Root")
root.add(sub)
root.add(f3)

root.show()
```

## 12 — Decorator Pattern

### 01_pizza.py
```python
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def desc(self):
        pass

class BasicPizza(Pizza):
    def cost(self):
        return 5

    def desc(self):
        return "Basic Pizza"

class Topping(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

class Cheese(Topping):
    def cost(self):
        return self.pizza.cost() + 2

    def desc(self):
        return self.pizza.desc() + " + Cheese"

class Olives(Topping):
    def cost(self):
        return self.pizza.cost() + 1

    def desc(self):
        return self.pizza.desc() + " + Olives"

class Chicken(Topping):
    def cost(self):
        return self.pizza.cost() + 3

    def desc(self):
        return self.pizza.desc() + " + Chicken"


p = BasicPizza()
p = Cheese(p)
p = Olives(p)
p = Chicken(p)
print(p.desc())
print(f"Total: ${p.cost()}")
```

## 13 — Template Method Pattern

### 01_recipe.py
```python
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
```

## 17 — Strategy Pattern

### 01_travel_strategy.py
```python
from abc import ABC, abstractmethod

class TravelStrategy(ABC):
    @abstractmethod
    def travel(self):
        pass

class Car(TravelStrategy):
    def travel(self):
        return "Going by Car"

class Bus(TravelStrategy):
    def travel(self):
        return "Going by Bus"

class Bike(TravelStrategy):
    def travel(self):
        return "Going by Bike"

class Traveler:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def go(self):
        return self.strategy.travel()


t = Traveler(Car())
print(t.go())

t.set_strategy(Bus())
print(t.go())

t.set_strategy(Bike())
print(t.go())
```

## 19 — State Pattern

### 01_light_switch.py
```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def toggle(self):
        pass

class OnState(State):
    def toggle(self):
        return OffState(), "Switched OFF"

class OffState(State):
    def toggle(self):
        return OnState(), "Switched ON"

class LightSwitch:
    def __init__(self):
        self.state = OffState()

    def press(self):
        new_state, msg = self.state.toggle()
        self.state = new_state
        return msg


switch = LightSwitch()
print(switch.press())
print(switch.press())
print(switch.press())
```
