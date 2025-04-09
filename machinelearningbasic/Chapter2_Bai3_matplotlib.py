# matplotlib: hien thi du lieu theo dang do thi bieu do

import matplotlib.pyplot as plt
import numpy as np

x = [3, 5]
y = [7, 9]

print(plt.plot(x, y))
plt.show() # hien do thi


image = np.random.rand(30, 30) # random ra mang 2 chieu 30x30 phan tu
plt.imshow(image)
plt.show()