import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([0, 0, 100, 0, 10, 10, 90, 10, 20, 20, 80, 20, 30, 30, 70, 30, 40, 40, 60, 40]) # defines the points on the x-axis
y_points = np.array([0, 100, 100, 0, 10, 90, 90, 10, 20, 80, 80, 20, 30, 70, 70, 30, 40, 60, 60, 40]) # defines the points on the y-axis

plt.plot(x_points, y_points) # plots the points as lines
# plt.plot(x_points, y_points, ls=":", c="r", lw="5") # dotted lines
# plt.plot(x_points, y_points, "o") # plots the points as dots
plt.show() # displays the graph