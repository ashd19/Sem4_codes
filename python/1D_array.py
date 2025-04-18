#using numpy
import numpy as np 

arr = np.array([1,23,4,4,5,5,23,12,33])
print("The array is : ",arr)
print("The type of the array is : ",type(arr))
print("The shape of the array is : ",arr.shape)
print("The dimension of the array is : ",arr.ndim)
print("The size of the array is : ",arr.size)
print("The data type of the array is : ",arr.dtype)
#Reshaping is the process of changing the shape of an array without changing the data.
print("The reshaped array is : ",arr.reshape(3,3))
print("Element at index 0 is : ",arr[0])   

new_array = np.zeros(5)
print("The new array of zeros with size 5 is : ",new_array)
# for i in range(5):
#     new_array[i] = int(input("Enter the element: "))

# print("The new array of zeros with size 5 is : ",new_array)
array_2 = np.arange(1,10,2)
print("Using arrange method:",array_2)
#what is arrange method?
#The arange() function returns an array with evenly spaced values within a given interval.

a3 = np.random.rand(5)
# for int values
a4 = np.random.randint(1,10,5)
print("The random array a4 is : ",a4)
print("The random array a3  is : ",a3)

a5 = np.empty(4)
print("The empty array is : ",a5)
#The empty() function returns a new array of given shape and type, without initializing entries.
a6 = np.full((2,2),5)
#The full() function returns a new array of given shape and type, filled with fill_value.
print("The full array is : ",a6)
a7 = np.eye(3)
#The eye() function returns a 2-D array with ones on the diagonal and zeros elsewhere.
print("The eye array is : ",a7)
a8 = np.identity(3)
#The identity() function returns a square array with ones on the diagonal and zeros elsewhere.
print("The identity array is : ",a8)
a9 = np.zeros((2,2))
# 2x2 matrix 
