list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter element: ")
    list.append(element)
print("The list is: ", list)
print("The first element is: ", list[0])
print("The last element is: ", list[-1])
print("The length of the list is: ", len(list))
print("The list in reverse order is: ", list[::-1])
print("The list in sorted order is: ", sorted(list))
print("The list in descending order is: ", sorted(list, reverse=True))
