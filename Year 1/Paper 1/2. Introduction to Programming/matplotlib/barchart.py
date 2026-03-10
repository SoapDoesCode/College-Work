import matplotlib.pyplot as plt
import numpy as np

x_points = np.array(["Fruits", "Starch", "Dairy", "Fats", "Protein"])
y_points = np.array([24, 19, 21, 22, 13])

plt.bar(x_points, y_points)
plt.show()