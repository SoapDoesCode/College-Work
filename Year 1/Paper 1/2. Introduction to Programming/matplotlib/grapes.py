import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./GRAPE_QUALITY.csv")

region = df['region']
quality = df['quality_score']
print(region)

x_points = np.array(region)
y_points = np.array(quality)

plt.plot(x_points, y_points, "o")
plt.show()