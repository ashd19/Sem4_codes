from scipy import linalg
from scipy.optimize import fsolve
import numpy as np
# what is optimize?
# optimize is a module in scipy that provides functions for optimization, root finding, and curve fitting.
def equation(x):

    return x*x - 9

# The initial guess in the context
#  of fsolve is the starting point for the algorithm 
# to begin searching for a solution (root) to the equation. 
# It is not the solution itself but rather a hint to guide the root-finding process.
root_1 = fsolve(equation, 0)
root_2 = fsolve(equation, -1)

print("Roots of the equation x^2 - 9 = 0 are:", root_1, root_2)

# solving a system of 3  linear equations 
# x = a^-1*b 
A = [[1, 1, 1], [1, -1, 1], [2, 3, 4]] # coefficient matrix
b = [1, 2, 1] # constant matrix
res = linalg.solve(A, b) 

# or 


# solving the system of equations
# to solve using the equations we find the inverse of a and multiply it with b
print("The solution of the system of equations is:", res)
a1 = linalg.inv(A) # finding the inverse of A
res1 =np.dot(a1,b)
print("The solution is:", res1)


#integrate x^2 from 0 to 1
from scipy.integrate import quad
def integrand(x):
    return x**2

result,error= quad(integrand, 0, 1)
#what is error?
#error is an estimate of the absolute error in the result of the integration.
# It provides a measure of how accurate the computed integral is.
print("The integral of x^2 from 0 to 1 is:", result)
print("Estimated error in the integral:", error)

# fourier transform
