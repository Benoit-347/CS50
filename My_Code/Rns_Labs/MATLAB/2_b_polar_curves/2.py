import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection = "polar")
x = np.arange(0, 2*np.pi, 0.001)
a = 3
y = a*np.sin(3*x)
plt.plot(x,y, 'b.')
plt.title("Graph of three leaved clover")
plt.show()