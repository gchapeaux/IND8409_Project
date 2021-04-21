import matplotlib.pyplot as plt
import numpy as np
from scripts.world import World
import gc
import keyboard

HEADLESS = True

def main():

    gc.enable()

    world = World('data/battleground.map')

    plt.ion()
    fig, axes = plt.subplots(2,3)
    for row in axes:
        for ax in row:
            ax.set_axis_off()
    if HEADLESS:
        plt.close()
    i=0
    while(plt.get_fignums()):
        if not(HEADLESS):
            fig.suptitle('Iteration '+str(i))
        world.step(axes, HEADLESS)
        plt.pause(1e-3)
        i += 1

    plt.ioff()
    plt.show()

main()