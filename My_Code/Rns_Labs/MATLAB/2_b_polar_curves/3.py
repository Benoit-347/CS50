import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection = 'polar')
x = np.arange(0, 2*np.pi, 0.001)
a = 5
y = a**2*np.cos(2*x)
plt.plot(x,y,'b.')
plt.title("Graph of lemniscate of bernoulli")
plt.show()