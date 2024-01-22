import numpy as np
import matplotlib.pyplot as plt

parameters = np.loadtxt("plot_data.txt", max_rows=1)
space_steps, time_step_space, time_steps = parameters

plot_data = np.loadtxt("plot_data.txt", skiprows=1)
plot_data = plot_data.T

space = np.linspace(0, 1, int(space_steps))
time = np.linspace(0, time_step_space, int(time_steps))

Time, Space = np.meshgrid(time, space)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Time, Space, plot_data, cmap='viridis') 

ax.set_xlabel('Time')
ax.set_ylabel('Space')
ax.set_zlabel('Temperature')
ax.set_title('Evolution over time and space')
plt.show()