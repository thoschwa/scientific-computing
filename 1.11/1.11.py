import numpy as np
import matplotlib.pyplot as plt
import scipy

def get_delta_t(delta_x, buffer):
    return 0.5 * np.square(delta_x) * buffer

space_steps = 101
    
delta_x = 1/(space_steps - 1)
delta_t = get_delta_t(delta_x, 0.5)

time_step_space = 0.3

time_steps = int(np.ceil(time_step_space / delta_t))

current_temperature = np.zeros(space_steps)
next_temperature = np.zeros(space_steps)
plot_data = []

current_temperature[0] = 350
current_temperature[-1] = 250

next_temperature[0] = 350
next_temperature[-1] = 250

alpha = delta_t / delta_x**2

A = np.zeros((space_steps - 2, space_steps - 2))
np.fill_diagonal(A, 1 + 2 * alpha)
np.fill_diagonal(A[:-1, 1:], -alpha)
np.fill_diagonal(A[1:, :-1], -alpha)

for i in range(space_steps - 2):
    j = (i + 1) * delta_x
    current_temperature[i + 1] = 350 - 100 * j + 200 * np.sin(np.pi * j)

# Time-stepping
plot_data = [current_temperature.copy()]
for t in range(time_steps):
    b = current_temperature[1:-1]
    # Adjust for boundary conditions in the vector b, if necessary
    b[0] += alpha * current_temperature[0]
    b[-1] += alpha * current_temperature[-1]
    next_temperature[1:-1] = scipy.linalg.solve(A, b)
    
    current_temperature = next_temperature.copy()
    plot_data.append(current_temperature.copy())

lower_diagonal = np.full(space_steps - 3, -alpha)
main_diagonal = np.full(space_steps - 2, 1 + 2 * alpha)
upper_diagonal = np.full(space_steps - 3, -alpha)

lower_diagonal_padded = np.append(lower_diagonal, 0)
upper_diagonal_padded = np.append(0, upper_diagonal)

A_banded = np.vstack((upper_diagonal_padded, main_diagonal, lower_diagonal_padded))

for i in range(1, space_steps - 1):
    j = i * delta_x
    current_temperature[i] = 350 - 100 * j + 200 * np.sin(np.pi * j)

plot_data = [current_temperature.copy()]
for t in range(time_steps):
    b = current_temperature[1:-1]

    b[0] += alpha * current_temperature[0]
    b[-1] += alpha * current_temperature[-1]

    next_temperature[1:-1] = scipy.linalg.solve_banded((1, 1), A_banded, b)

    current_temperature = next_temperature.copy()
    plot_data.append(current_temperature.copy())

#plotting
data_np = np.array(plot_data)
data_np = data_np.T 

space = np.linspace(0, 1, space_steps)
time = np.linspace(0, time_step_space, time_steps + 1)

Time, Space = np.meshgrid(time, space)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Time, Space, data_np, cmap='viridis') 

ax.set_xlabel('Time')
ax.set_ylabel('Space')
ax.set_zlabel('Temperature')
ax.set_title('Evolution over time and space')
plt.show()

#plotting
data_np = np.array(plot_data)
data_np = data_np.T 

space = np.linspace(0, 1, space_steps)
time = np.linspace(0, 1, time_steps)

# Plotting for discrete timestamp values
for t in range(0, time_steps, 1000):  # Change the step size as per your requirement
    plt.plot(space, data_np[:, t], label=f'Time={t}')

plt.xlabel('Space')
plt.ylabel('Value')
plt.title('Evolution over space')
plt.legend()
plt.show()