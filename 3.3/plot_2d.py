import numpy as np
import matplotlib.pyplot as plt

# Load plot parameters from first row of file
parameters = np.loadtxt("plot_data.txt", max_rows=1)
space_steps, time_step_space, time_steps = parameters

# Load plot data from the rest of the file
plot_data = np.loadtxt("plot_data.txt", skiprows=1)
plot_data = plot_data.T 

# Create space array
space = np.linspace(0, 1, int(space_steps))

# Plotting 2D
for t in range(0, int(time_steps), 1000):
    plt.plot(space, plot_data[:, t], label=f'Time={t}')

plt.xlabel('Space')
plt.ylabel('Value')
plt.title('Evolution over space')
plt.legend()
plt.show()