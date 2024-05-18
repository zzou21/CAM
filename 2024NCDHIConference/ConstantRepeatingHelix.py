# This graphs the Constant Repeating Helix, Coordinate Axes Model Type 1 simulation

import numpy as np
import matplotlib.pyplot as plt

# Original func with phase shift
def graphA(x, phase=0):
    return np.sin(x + phase)

# Rotation angle in radians
theta = np.pi / 4

def rotateXValue(x, y):
    return x * np.cos(theta) - y * np.sin(theta)
def rotateYValue(x, y):
    return x * np.sin(theta) + y * np.cos(theta)

x_values = np.linspace(0, 30, 500)
y_values = graphA(x_values)

y_values_shifted = graphA(x_values, phase=np.pi/4)
x_rotated = rotateXValue(x_values, y_values)
y_rotated = rotateYValue(x_values, y_values)

horizShiftValue = 1

# Combine the rotated X and Y values. Don't forget to turn the y values into negative numbers to form the helix
x_rotated_shifted = rotateXValue(x_values + horizShiftValue, -y_values_shifted)
y_rotated_shifted = rotateYValue(x_values + horizShiftValue, -y_values_shifted)

plt.figure(figsize=(8, 8))
plt.plot(x_rotated, y_rotated, label='Humanism', color='blue')
plt.plot(x_rotated_shifted, y_rotated_shifted, label='Materialism', color='red')
plt.title('Constant Repeating Helix')
plt.xlabel('Time')
plt.ylabel('Number of Relations')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()