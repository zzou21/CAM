# This creates the graph for the case study for war memoirs written during the 1990s.

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Draw the horizontal line of the box
x_limited = np.linspace(0, 7, 200)
y = np.full_like(x_limited, 2)
ax.plot(x_limited, y, "r", label='y = 2')

# Draw the vertical line of the box
y_vertical = np.linspace(0, 2, 200)
x_vertical = np.full_like(y_vertical, 7)
ax.plot(x_vertical, y_vertical, 'r', label='x = 5')

ax.text(4.5, 1, 'War Memoir, 1990', fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
ax.set_xlabel('Humanism', fontsize=12)
ax.set_ylabel('Materialism', fontsize=12)
ax.xaxis.set_label_coords(0.5, -0.05)
ax.yaxis.set_label_coords(-0.05, 0.5)
plt.show()