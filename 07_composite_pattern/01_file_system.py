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
