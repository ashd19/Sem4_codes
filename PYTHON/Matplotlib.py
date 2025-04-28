import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8, 5])
ypoints = np.array([3, 5, 7, 9, 11])

plt.plot(
    xpoints, 
    ypoints, 
    marker='o', 
    ms=10,         # Marker size
    mec='r',       # Marker edge color
    mfc='b',       # Marker face color
    linestyle='dotted', 
    linewidth=2, 
    color='red'    # Line color
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")  

plt.show()
