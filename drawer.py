from matplotlib import pyplot as plt

'''
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = [3.675, 4]
y = [3, 2]
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid()
plt.plot(x, marker="o", markersize=10, markerfacecolor="red")
plt.show()
'''

# Define the coordinates of the point
plt.xlim(0, 5)
plt.ylim(0, 5)
x = 2
y = 3

# Plot the point
plt.scatter(x, y)

# Display the plot
plt.show()