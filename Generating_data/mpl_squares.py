import matplotlib.pyplot as plt
import numpy as np

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] #x -> indici dell'array  Y-> valore assunto in quell'indice

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
ax.tick_params(axis= 'both', labelsize = 14)

#ax.plot(squares)

plt.show()
