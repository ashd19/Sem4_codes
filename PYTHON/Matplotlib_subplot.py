import matplotlib.pyplot as plt
import numpy as np

# First subplot
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot(y, x)

# Second subplot
x = np.array([1, 2])
y = np.array([5, 6])

plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd plot
plt.plot(y, x)


plt.show()
