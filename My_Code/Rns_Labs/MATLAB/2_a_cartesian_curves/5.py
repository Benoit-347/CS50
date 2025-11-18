import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 1000)
r = 5
y = (r**2-x**2)**0.5
z = (r**2-x**2)**0.5*-1
#plt.figure(figsize=(8.5, 10))
fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.plot(x,y)
plt.plot(x,z)
plt.title("Graph of Circle")
plt.legend()
plt.grid()
plt.show()