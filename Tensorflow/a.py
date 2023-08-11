import matplotlib.pyplot as plt
import numpy as np

a = np.array([0, 64, 128, 255]).reshape(2, 2)
plt.imshow(a, cmap = "gray")
plt.show()