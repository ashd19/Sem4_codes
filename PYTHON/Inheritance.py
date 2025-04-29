class Animal:
    def char(self):
        print("Is an animal")


class dog(Animal):	
    def sound(self):
        print("Bark Bark")



d = dog()
print("The dog ",end="")
d.char()
d.sound() 

#2nd 2. Multilevel Inheritance
# A class inherits from a class,
#  which itself inherits from another class.
# same code only 
class puppy(dog):
    def s(self):
        print("shing shlong")
p=puppy()
p.sound()
p.char()
p.s()

#3Multiple Inheritance

# A class inherits from more than one parent class.
class Father:
    def car(self):
        print("Father's car")

class Mother:
    def house(self):
        print("Mother's house")


class son(Father,Mother):
    def s():
        print("wowmwm")


a = son()
a.car()
a.house()

#4 Hierarchical Inheritance
# a super class is inhereited by multiple subclasses.

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")




class CustomList(list):
    def __iadd__(self, other):
        self.append(other)
        return self

# Take initial input list
raw_input = input("Enter initial elements separated by space: ")
l1 = CustomList(raw_input.split())  # All elements are strings initially

# Take another value to add using +=
new_element = input("Enter a value to add using += : ")
l1 += new_element  # Calls __iadd__

print("Updated list:", l1)



class Calculator:
    def add(self, *args):
        return sum(args) 
    


    