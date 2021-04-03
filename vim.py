
import math
import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(1,2*math.pi,100)
b = np.sin(a)

plt.plot(a,b)
plt.show()

