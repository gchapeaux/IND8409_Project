import matplotlib.pyplot as plt
import numpy as np
from scripts.world import World

world = World('data/battleground.map')

plt.ion()
fig, axes = plt.subplots(2,3)
for row in axes:
    for ax in row:
        ax.set_axis_off()

for _ in range(30):
    world.step(axes)
    plt.pause(5)

plt.ioff()
plt.show()