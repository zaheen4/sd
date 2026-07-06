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
