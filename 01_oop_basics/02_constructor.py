class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

s1 = Student("Tony Stark", 3.55)
s2 = Student("Iron Man", 2.22)

print(s1.name, s1.cgpa)
print(s2.name, s2.cgpa)
