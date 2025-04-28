import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 15, 25, 25])

mylabels = ["Mumbai", "Surat", "Bengaluru", "Jaipur"]
myexplode = [0.1, 0, 0, 0]
mycolors = ["blue", "white", "black", "hotpink"]

plt.pie(
    x,
    labels=mylabels,
    startangle=90,
    explode=myexplode,
    shadow=True,  # shadow must be True/False, not a list
    colors=mycolors
)

plt.legend(loc="lower left")
# plt.legend(bbox_to_anchor=(1, 3, 1))  # (optional) Fix typo: bbox_to_anchor
plt.show()
