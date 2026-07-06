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
