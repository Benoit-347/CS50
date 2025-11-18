import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 1000) #syn: linspace(<start>,<stop>,<num_of_seq>)
y = np.sin(x)       #creates a seq of evently spaces numbers (no. of seq is given in 3rd para)
z = np.cos(x)
plt.plot(x,y, label = "y = sin(x)") #label is used to show the line of plot = the keyword "label" value
plt.plot(x,z, label = "z = cos(x)") #note label requires legend
plt.title("Grapth of sin and cos")  #Shows text in string as title
plt.legend()    #shows visual representation of different data plots of graph (also pulls data from label)
plt.grid()   #shows a grid to view straight lines from values
plt.show()  #produces the graph ui / graphical output