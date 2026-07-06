class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def good_morning(self):
        return self.name

s1 = Student("Tony Stark", 3.55)
print(s1.good_morning())
