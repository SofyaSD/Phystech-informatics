#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5,5,0.01)
plt.plot(x,x**2 - x - 6)
print(np.roots([1,-1,-6]))
plt.grid()
plt.show()
