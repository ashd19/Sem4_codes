#dictionary us3ed to store key value pairs
# #A dictionary is a collection which is unordered, changeable and does not allow duplicates.

print("Consider a dictionary of key-value pairs, where the key is the roll no of the student and  name is the values: ") 
dict ={
    26 : "raj",
    27 : "ram",
    28 : "rajesh",
    29 : "rajendra",
    30 : "rajat",
    31 : "rajkumar",
    32 : "rajeshwari",
    33 : "rajeshwari",

}
print(dict)
print("The type of collection data type is : ",type(dict))
print("The length of the dictionary is : ",len(dict))
print("The roll no of the students  are : ",dict.keys())
print("The corresponding names  of the students  are : ",dict.values())
print("The items in the dictionary are : ",dict.items())
print("the name of roll no 26 is : ",dict[26])
print("The name of roll no 27 is : ",dict.get(27))
name = input("Enter the name  of the student you want to know the rollno of :")

for rollno,name1 in dict.items():
    if name1 == name:
        print("The roll no of the ",name," is : ",rollno)
        break

dict.update({34:"rajat"})
print("The updated dictionary is : ",dict)
dict.pop(34)
print("The dictionary after deleting the roll no 34 is : ",dict)
dict.popitem()
print("The dictionary after deleting the last item is : ",dict)
dict1 = dict.copy()
print("The copied dictionary is : ",dict1)
dict.clear()
print("The dictionary after clearing all the items is : ",dict)
keys1 = [1,2,3,4,5]
values1 = ["raj","ram","rajesh","rajendra","rajat"]
dict2 = dict.fromkeys(keys1,values1)
print("The dictionary created from keys and values is : ",dict2)