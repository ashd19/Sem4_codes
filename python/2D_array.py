import numpy as np
#what is axis in numpy?
#axis = 0 is the row axis, axis = 1 is the column axis
#axis = 2 is the depth axis (for 3D arrays)

matrix = np.array([[123,43,1],[14,41,12],[143,25,13]])
print("Original 2D array : \n",matrix)
print("The dimensions are : ",matrix.shape) # (2, 3)
print("The element at (0,1) is  : ",matrix[0, 1]) 
print("Sorted matrix : ",np.sort(matrix)) # sort along the last axis (default)
print("Sum of matrix elements : ",np.sum(matrix)) 
print("Maximum element in matrix : ",np.max(matrix))
print("Minimum element in matrix : ",np.min(matrix))
print("Mean of matrix elements : ",np.mean(matrix))
print("Standard deviation of matrix elements : ",np.std(matrix))
print("Transpose of matrix : ",np.transpose(matrix))
print("Inverse of matrix : ",np.linalg.inv(matrix)) # inverse of a matrix
print("Determinant of matrix : ",np.linalg.det(matrix)) # determinant of a matrix
print("Eigen values of matrix : ",np.linalg.eig(matrix)) # eigen values of a matrix
print("Trace of matrix : ",np.trace(matrix)) # trace of a matrix
print("Rank of matrix : ",np.linalg.matrix_rank(matrix)) # rank of a matrix
print("Diagonal of matrix : ",np.diag(matrix)) # diagonal of a matrix

#flattening the matrix means converting a 2D array into a 1D array
print("Flattened matrix : ",matrix.flatten()) # flatten the matrix
print("Deleting the first row : ",np.delete(matrix, 0, axis=0)) # 0 is the index of row 
print("Deleting the first column : ",np.delete(matrix, 0, axis=1)) # delete the first column
print("Adding a new row : ",np.append(matrix, [[1,2,3]], axis=0)) # add a new row
print("Adding a new column : ",np.append(matrix, [[1],[2],[3]], axis=1)) # add a new column



#make a 3x3 matrix 
#a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])