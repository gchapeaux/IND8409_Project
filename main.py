import matplotlib.pyplot as plt
import numpy as np
from scripts.world import World
from scripts.mapreader import viz_map
import gc
import keyboard
import os

#Region[Red] Save paths

if not os.path.exists('output'):
        os.makedirs('output')
output_path = './output'

#EndRegion

#Region[Cyan] Main

run_dict = { 0 : '|', 1 : '/', 2 : '-', 3 : '\\', 4 : '|', 5 : '/', 6 : '-', 7 : '\\' }

def main(HEADLESS=True, SAVING=True):

    gc.enable()
    escape = False
    i=0

    world = World('data/battleground.map', n_robots=50, spawn_radius=50)

    print("| World generated, entering simulation")
    
    fig, axes = plt.subplots(2,3)
    if not(HEADLESS):
        plt.ion()
        for row in axes:
            for ax in row:
                ax.set_axis_off()

    while not(escape) and (HEADLESS or plt.get_fignums()):
        try:
            escape = keyboard.is_pressed("esc")
        except:
            escape = False
        if (i%10 == 0):
            print('| Simulation running, press ESCAPE to end |{}|'.format(run_dict[(i//10)%8]), end='\r')
        world.step(fig, axes, HEADLESS, i)
        i += 1

    if SAVING:
        plt.close()
        
        viz_map(world.worldMap, "Global world map", os.path.join(output_path, "world.png"))
        
        map_size = world.worldMap.shape[0]*world.worldMap.shape[1]
        completion = {}
        
        for robot in world.robots.values():
            
            save_path = os.path.join(output_path, "map_robot_{}_.png".format(robot.id))
            fig_name = "Map of the robot {} after {} steps".format(robot.id, i)
            viz_map(robot.dynamicMap.map, fig_name, save_path)

            completion[robot.id] = np.array(robot.exploration_history)/map_size

        for rid, hist in completion.items():
            np.random.seed(rid)
            color = list(np.random.choice(range(256), size=3))
            plt.plot(hist, color=color)


    if not(HEADLESS):
        plt.ioff()
    print("| Simulation ended. Check robot maps in output folder.")
#EndRegion

main()