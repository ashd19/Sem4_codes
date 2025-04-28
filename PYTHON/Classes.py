
class Student:
    name = "Naitik"
    age = 19
    roll_no = 5

s1 = Student()
s1.name = "Naitik Mehta"

print(f"{s1.name} having Roll_No. {s1.roll_no} is {s1.age} years old.")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def statement(self):
        print(f"{self.name} is {self.age} years old.")

a = Person("Naitik", 19)
a.statement()


class Result:
    def __init__(self, name, roll_no, marks1, marks2, marks3):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total(self):
        self.t = self.marks1 + self.marks2 + self.marks3
        print("Total =", self.t)

    def percentage(self):
        self.p = self.t * 100 / 300
        print("Percentage =", self.p)

    def grade(self):
        if self.p >= 90:
            print("Grade: A")
        elif self.p >= 75:
            print("Grade: B")
        else:
            print("Grade: Less than B")

    def call(self):
        self.total()
        self.percentage()
        self.grade()

a = Result("Naitik", 5, 80, 80, 80)  
a.call()


class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        ar = self.radius * self.radius * 3.14
        print("Area of Circle =", ar)

radius = int(input("Enter the radius of the circle: "))
a = Circle(radius)
a.area()
