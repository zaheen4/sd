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
