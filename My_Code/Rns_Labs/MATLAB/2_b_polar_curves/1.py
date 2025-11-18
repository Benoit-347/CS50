import matplotlib.pyplot as plt
import numpy as np
plt.axes(projection = "polar")  #to customize individual axes in a figure (control for advanced plot layouts.)
a = 5                           #Only required if using plot() not req if using plt.polar()
t = np.arange(0,2*np.pi,0.001)  #syn: arange(<start>, <stop>, <step>)
r = a - a*np.cos(t)    #creates a seq of values with step value from 3rd para (similar to range but also has floating point values)
plt.polar(t,r, 'g.')
s = a+a*np.cos(t)
plt.polar(t,s,"y.")
plt.title("Graph of cardiod")
plt.show()