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
