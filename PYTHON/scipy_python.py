import numpy as np
from scipy.linalg import solve, eig
from scipy.optimize import minimize
from scipy.integrate import quad
from scipy.interpolate import interp1d


A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6])
x = solve(A, b)

eigvals, eigvecs = eig(A)

f = lambda x: (x - 2) ** 2
res = minimize(f, x0=0)


integral, _ = quad(np.sin, 0, np.pi)


x_data = np.linspace(0, 10, 10)
y_data = np.sin(x_data)
interp_func = interp1d(x_data, y_data, kind='cubic')
y_interp = interp_func(5)

print(f"Solution x: {x}")
print(f"Eigenvalues: {eigvals}")
print(f"Minimization result: {res.x}")
print(f"Integral of sin(x): {integral}")
print(f"Interpolated value at x=5: {y_interp}")



