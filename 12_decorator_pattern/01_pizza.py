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
