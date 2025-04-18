my_list = []

n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)

print("The list is:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Length:", len(my_list))
print("Reversed list:", my_list[::-1])
print("Sorted list:", sorted(my_list))
print("Descending:", sorted(my_list, reverse=True))

a = input("Enter the element to be searched: ")
if a in my_list:
    print("Element is present")
else:
    print("Element is not present")

b = input("Enter the element to be deleted: ")
if b in my_list:
    my_list.remove(b)
    print("Element deleted:", my_list)
else:
    print("Element not found")

# String methods
names = ["raj", "ram", "rajesh"]
print("Original names:", names)
print("Upper:", [name.upper() for name in names])
print("Lower:", [name.lower() for name in names])
print("Title:", [name.title() for name in names])
print("Swapcase:", [name.swapcase() for name in names])

# More list operations
my_list.append("raj")
print("After append:", my_list)

my_list.insert(2, "ram")
print("After insert at index 2:", my_list)

my_list.extend(["rajesh", "raj"])
print("After extend:", my_list)

my_list.remove("raj")
print("After remove:", my_list)

print("Popped element:", my_list.pop())
print("After pop:", my_list)
print("Popped element at index 2:", my_list.pop(2))
print("After pop at index 2:", my_list)


list_copy = my_list.copy()
list_copy.clear()
print("After clear (copy):", list_copy)

print("Original list:", my_list)
my_list.reverse()
print("After reverse:", my_list)

my_list.sort()
print("After sort:", my_list)

print("Count of 'raj':", my_list.count("raj"))
my_list.append("raj")
print("Index of 'raj':", my_list.index("raj"))
print("Sliced list (first 3):", my_list[0:3])

print("Concatenated with names:", my_list + names)
print("Repeated list:", my_list * 2)
print("'raj' in list?", "raj" in my_list)
