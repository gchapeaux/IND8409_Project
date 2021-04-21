import numpy as np
import matplotlib.pyplot as plt
from scripts.robot import Robot
from scripts.mapreader import read_map, viz_map, viz_map_subp
from scripts.dynamicmap import Dir

class World:

    def __init__(self, path_to_map, n_robots=6):

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
            ca_robot = tuple(np.random.randint(0, len(self.worldMap)//2,2))
            while self.occupationMap[ca_robot]:
                ca_robot = tuple(np.random.randint(0, len(self.worldMap)//2,2))
            self.occupationMap[ca_robot] = True
            self.coords[key] = ca_robot


    def step(self, axes):
        for robot in self.robots.values():
            self.__moving(robot)
            #self.__sense(robot)
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

        if dir == Dir.NORTH:
            xa_robot = xa_robot - 1
            self.coords[robot.id] = (xa_robot, ya_robot)
        elif dir == Dir.EAST:
            ya_robot = ya_robot + 1
            self.coords[robot.id] = (xa_robot, ya_robot)
        elif dir == Dir.SOUTH:
            xa_robot = xa_robot + 1
            self.coords[robot.id] = (xa_robot, ya_robot)
        elif dir == Dir.WEST:
            ya_robot = ya_robot - 1
            self.coords[robot.id] = (xa_robot, ya_robot)

    def __sense(self, robot):
        xa_robot, ya_robot = self.coords[robot.id]
        sensors = np.zeros((3,3), dtype=str)
        for i in range(3):
                for j in range(3):
                    if (xa_robot-1+i >=0 and xa_robot-1+i < self.worldMap.shape[0] and ya_robot-1+j >=0 and ya_robot-1+j < self.worldMap.shape[1]):
                        sensors[i,j] = self.worldMap[xa_robot-1+i, ya_robot-1+j]

        self.robots[robot.id].sense_world(sensors)

    def sense2

    def __communicate(self):
        print("Pouet")

    def __visualize(self, axes, radius = 50):
        plots = {
            1 : (0,0),
            2 : (0,1),
            3 : (0,2),
            4 : (1,0),
            5 : (1,1),
            6 : (1,2)
        }
        for plot in plots.items():
            viz_map_subp(self.robots[plot.key()].dynamicMap.map_extract(radius), axes[l][c])
        plt.draw()
