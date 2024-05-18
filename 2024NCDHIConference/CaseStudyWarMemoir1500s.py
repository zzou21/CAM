# This creates the graph for the case study for war memoirs written during the 1500s.

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

setLinspaceLimited = np.linspace(0, 3, 200)
y = np.full_like(setLinspaceLimited, 7)
plt.plot(setLinspaceLimited, y, "r")

y_vertical = np.linspace(0, 7, 200)
x_vertical = np.full_like(y_vertical, 3)
plt.plot(x_vertical, y_vertical, 'r')
plt.text(2, 1, 'War Memoir, 1550', fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

ax.set_xlabel('Humanism', fontsize=12)
ax.set_ylabel('Materialism', fontsize=12)
ax.xaxis.set_label_coords(0.5, -0.05)
ax.yaxis.set_label_coords(-0.05, 0.5)
plt.show()