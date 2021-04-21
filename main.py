from scripts.world import World

world = World('data/battleground.map')
print("World generated")

for _ in range(15):
    world.step()