import numpy as np
import matplotlib.pyplot as plt

#enter for example "plot_data_beginning.txt"
filename = input("Enter the name of the file: ")

parameters = np.loadtxt(filename, max_rows=1)
space_steps, time_step_space, time_steps = parameters

plot_data = np.loadtxt(filename, skiprows=1)
plot_data = plot_data.T

data_np = np.array(plot_data)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, 1, int(space_steps))
y = np.linspace(0, 1, int(space_steps))
xg, yg = np.meshgrid(x, y)
ax.plot_surface(xg, yg, data_np, cmap='afmhot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Temperature')
plt.show()