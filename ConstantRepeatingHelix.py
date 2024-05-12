#Constant helix

import numpy as np
import matplotlib.pyplot as plt

# Define the original function with a phase shift parameter
def g(x, phase=0):
    return np.sin(x + phase)

# Define the rotation angle in radians
theta = np.pi / 4

# Define the rotation transformations
def rotate_x(x, y):
    return x * np.cos(theta) - y * np.sin(theta)

def rotate_y(x, y):
    return x * np.sin(theta) + y * np.cos(theta)

# Generate x values
x_values = np.linspace(0, 30, 400)
# Compute the original y values without phase shift
y_values = g(x_values)

# Compute the original y values with phase shift
y_values_shifted = g(x_values, phase=np.pi/4)

# Compute the rotated x and y values
x_rotated = rotate_x(x_values, y_values)
y_rotated = rotate_y(x_values, y_values)

# This variable provides a horizontal shift value
horizShiftValue = 1

# Compute the rotated x and y values with phase shift
x_rotated_shifted = rotate_x(x_values + horizShiftValue, -y_values_shifted)
y_rotated_shifted = rotate_y(x_values + horizShiftValue, -y_values_shifted)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_rotated, y_rotated, label='Original Function Rotated', color='blue')
plt.plot(x_rotated_shifted, y_rotated_shifted, label='Shifted Function Rotated', color='red')
plt.title('Double Helix Illusion in 2D')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')  # This ensures that the aspect ratio is equal
plt.show()