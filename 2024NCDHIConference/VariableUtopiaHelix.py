# This graphs the Variable "Utopia" Helix, Coordinate Axes Model Type 2 simulation

import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def graphA(x):
    # The "exp"" is a dampening factor to create the image that the graphs are closing in on each other to form a straight line
    return np.sin(x) * np.exp(-0.1 * x)

theta = np.pi / 4

def rotateXValue(x, y):
    return x * np.cos(theta) - y * np.sin(theta)
def rotateYValue(x, y):
    return x * np.sin(theta) + y * np.cos(theta)

x_values = np.linspace(0, 30, 500)
y_g = graphA(x_values)

# Put rotations onto standard graph
x_rotated_g = rotateXValue(x_values, y_g)
y_rotated_g = rotateYValue(x_values, y_g)

# Apply rotation and reflection to the standard graph. Don't forget to turn Y values into negative numbers by adding a negative sign
x_rotated_g_reflected = rotateXValue(x_values, -y_g)
y_rotated_g_reflected = rotateYValue(x_values, -y_g)

plt.figure(figsize=(8, 8))
plt.plot(x_rotated_g, y_rotated_g, label='Humanism', color='blue')
plt.plot(x_rotated_g_reflected, y_rotated_g_reflected, label='Materialism', color='red')
plt.title('Variable \"Utopia\" Helix')
plt.xlabel('Time')
plt.ylabel('Number of Relations')
plt.axhline(0, color='black', linewidth=0.25)
plt.axvline(0, color='black', linewidth=0.25)
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()