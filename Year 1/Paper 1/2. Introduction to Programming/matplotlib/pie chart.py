import matplotlib.pyplot as plt
import numpy as np

labels = np.array(["Fruits", "Starch", "Dairy", "Fats", "Protein"])
x_points = np.array([24, 19, 21, 22, 13])
colours = [
    [0.333, 0.804, 0.988, 0.65],
    [0.969, 0.659, 0.722, 0.65],
    [1.0, 1.0, 1.0, 0.6],
    [0.969, 0.659, 0.722, 0.65],
    [0.333, 0.804, 0.988, 0.65],
]

plt.pie(x_points, labels=labels, colors=colours)
plt.legend(title="Foods")
plt.show()