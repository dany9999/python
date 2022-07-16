
import matplotlib.pyplot as plt

#writing lists by hand can be inefficient, especially when we have many points

#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]

#let's use loop in python

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#ax.scatter(x_values, y_values, c='red', s=10)  #singoli punti   #s ---> size   #c ---> color
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) #cmap --> 

#set chart title and label axes
ax.set_title("square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set the range for each axis

ax.axis([0, 1100, 0, 1100000])

plt.show()

#plt.savefig('squaree_plot.png', bbox_inches='tight')   #####salva come file il plot image