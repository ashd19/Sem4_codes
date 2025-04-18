#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuple items are ordered, unchangeable, and allow duplicate values.

myfruits= ("apple", "banana", "cherry", "apple", "cherry")
print(myfruits)
print(type(myfruits))
print(len(myfruits))
print(myfruits[0])
print(myfruits[-1])
print(myfruits[2:5])
print(myfruits[:3])
print(myfruits[1:])
#it can contain combinations of data types
t = (1,2,4,5)
print("Maximum value in tuple:", max(t))
print("Minimum value in tuple:", min(t))
print("Sum of tuple:", sum(t))
print("Sorted tuple:", sorted(t))
print("Tuple with one item:", (1,))
print("Tuple with one item:", (1,2))
print("Reversed tuple",tuple(reversed(t)))
print("Converting list to tuple:", tuple([1,2,3]))  
print("Adding two tuples:", t + (6,7,8))
print("Multiplying tuple:", t * 2)
print("Checking if 2 is in tuple:", 2 in t)
print("Adding two tuples using zip:", list(zip(t, (6,7,8))))
#why list is used here ?
#because zip returns an iterator of tuples, so we convert it to list to see the output.
#tuples are immutable
#myfruits[0] = "orange" #this will give an error
#what is enumerate?
#enumerate() adds a counter to an iterable and returns it in the form of an enumerate object.
print("Enumerate tuple:", list(enumerate(myfruits)))
#what is any and all ? 
#any() returns True if any element of the iterable is true. If not, it returns False.
#all() returns True if all elements of the iterable are true. If not, it returns False.
print("Any in tuple:", any(myfruits))
print("All in tuple:", all(myfruits))
#what is tuple unpacking?   
#Tuple unpacking is a way to assign values from a tuple to multiple variables in a single statement.
#It allows you to extract values from a tuple and assign them to individual variables.
print("Count of apple in tuple:", myfruits.count("apple"))
print("Index of apple in tuple:", myfruits.index("apple"))

