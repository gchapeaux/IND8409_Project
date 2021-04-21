import numpy as np
import matplotlib.pyplot as plt
from scripts.robot import Robot
from scripts.mapreader import read_map, viz_map, viz_map_robot
from scripts.dynamicmap import Dir

class World:

    def __init__(self, path_to_map, n_robots=6, spawn_radius = 30):

        # worldMap : strings matrix describing the world
        self.worldMap = read_map(path_to_map)

        # occupationMap : bool matrix describing which cases are available
        self.occupationMap = np.where(self.worldMap == '@', True, False)

        # robots : dict containing all robots
        self.robots = {}
        rid = 0
        while rid < n_robots:
            self.robots[rid] = Robot(rid)
            rid = rid+1

        # coords : dict containing robot coordinates
        self.coords = {}
        for key in self.robots.keys():
            ca_robot = tuple(np.random.randint(len(self.worldMap)//2-spawn_radius, len(self.worldMap)//2+spawn_radius, 2))
            while self.occupationMap[ca_robot]:
                ca_robot = tuple(np.random.randint(len(self.worldMap)//2-spawn_radius, len(self.worldMap)//2+spawn_radius, 2))
            self.occupationMap[ca_robot] = True
            self.coords[key] = ca_robot


    def step(self, axes, headless):
        for robot in self.robots.values():
            self.__moving(robot)
            self.__sense(robot)
        self.__communicate()
        if not(headless):
            self.__visualize(axes)


    '''

        | y-1   y   y+1
    ----|-------------
    x-1 |       N
     x  |  W   [R]   E
    x+1 |       S

    '''

    def __moving(self, robot):
        possible_directions = []
        xa_robot, ya_robot = self.coords[robot.id]

        if xa_robot > 0 and not(self.occupationMap[(xa_robot - 1, ya_robot)]):
            possible_directions.append(Dir.NORTH)
        if ya_robot < self.worldMap.shape[1] - 1 and not(self.occupationMap[(xa_robot, ya_robot + 1)]):
            possible_directions.append(Dir.EAST)
        if xa_robot < self.worldMap.shape[0] - 1 and not(self.occupationMap[(xa_robot + 1, ya_robot)]):
            possible_directions.append(Dir.SOUTH)
        if ya_robot > 0 and not(self.occupationMap[(xa_robot, ya_robot - 1)]):
            possible_directions.append(Dir.WEST)
        move = self.robots[robot.id].move(possible_directions)
        
        if move == Dir.NORTH:
            self.coords[robot.id] = (xa_robot - 1, ya_robot)
        elif move == Dir.EAST:
            self.coords[robot.id] = (xa_robot, ya_robot + 1)
        elif move == Dir.SOUTH:
            self.coords[robot.id] = (xa_robot + 1, ya_robot)
        elif move == Dir.WEST:
            self.coords[robot.id] = (xa_robot, ya_robot - 1)

    def __sense(self, robot, rad_sensor=5) :
        xa_robot, ya_robot = self.coords[robot.id]
        sensors = np.zeros((rad_sensor * 2 + 1,rad_sensor * 2 + 1), dtype=str)
        for i in range(rad_sensor * 2 + 1):
                for j in range(rad_sensor * 2 + 1):
                    if (xa_robot - rad_sensor + i >= 0 and xa_robot - rad_sensor+i < self.worldMap.shape[0] and ya_robot - rad_sensor + j >= 0 and ya_robot-rad_sensor + j < self.worldMap.shape[1]):
                        sensors[i,j] = self.worldMap[xa_robot - rad_sensor + i, ya_robot - rad_sensor + j]
        
        self.robots[robot.id].sense_world(sensors)
    
    def __distManhatan(self, coords1,coords2):
        return abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1])

    def __communicate(self):
        for key1 in self.coords.keys():
            for key2 in  self.coords.keys():
                if key1 != key2:
                    if self.__distManhatan(self.coords[key1],self.coords[key2]) < 7:
                        #print("Merge "+str(key1)+" with "+str(key2))
                        cc_robot2 = tuple(i-j for (i,j) in zip(self.coords[key2], self.coords[key1]))
                        self.robots[key1].mergeMaps(self.robots[key2].dynamicMap, cc_robot2)

    def __visualize(self, axes, radius = 10):
        plots = {
            0 : (0,0),
            1 : (0,1),
            2 : (0,2),
            3 : (1,0),
            4 : (1,1),
            5 : (1,2)
        }
        for plot in plots.items():
            viz_map_robot(self.robots[plot[0]], axes[plot[1]], radius)
        plt.draw()
