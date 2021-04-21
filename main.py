import matplotlib.pyplot as plt
from scripts.world import World

world = World('data/battleground.map')
print("World generated")

plt.ion()
fig, axes = plt.subplots(2,3)

for _ in range(30):
    world.step(axes)
    plt.pause(1e-3)

plt.ioff()
plt.show()