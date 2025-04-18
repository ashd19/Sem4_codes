#sets are an unordered collection of unique elements    
#sets are mutable, meaning you can add or remove items from them.
# only distince values .....
set1 = {1, 2, 3, 4, 5,5,6,}
print("Sets only contain unique values :",set1)
print("Type of set1:", type(set1))
print("Length of set1:", len(set1))
print("Converting list to set: ", set([1, 2, 3, 4, 5, 5]))
print("Converting tuple to set: ", set((1, 2, 3, 4, 5, 5)))
print("Converting string to set: ", set("hello"))
print("Adding element to set: ", set1.add(7))
print("Set after adding element: ", set1)
print("Removing element from set: ", set1.remove(7))
print("Set after removing element: ", set1)
print("Discarding element from set: ", set1.discard(5))
print("Set after discarding element: ", set1)
print("Popping element from set: ", set1.pop())
print("Set after popping element: ", set1)
print("Clearing set: ", set1.clear())
print("Set after clearing: ", set1)
a = {1, 2, 3}
b = {3, 4, 5}
print("Set a :", a)
print("Set b :", b)
print("Union of a and b: ", a.union(b))
print("Intersection of a and b: ", a.intersection(b))
print("Difference of a and b: ", a.difference(b))
print("Symmetric difference of a and b: ", a.symmetric_difference(b))
print("Subset of a: ", a.issubset(b))
print("Superset of a: ", a.issuperset(b))
print("Disjoint set of a and b: ", a.isdisjoint(b))
print("Copying set a to set c: ", a.copy())
print("Set a after copying to set c: ", a)
#subset is a set that contains only elements that are also in another set.
#superset is a set that contains all elements of another set.
#update() method adds elements from one set to another set.
#This is printing None because the update() method updates the set in-place and does not return anything (i.e., it returns None).
a.update(b)
print("Set a after updating with set b: ", a)
