import numpy as np
import random as rd
from enum import Enum, auto
from scripts.dynamicmap import DynamicMap, Dir

class Robot:

    def __init__(self, id, dynamicMap=None):
        self.id = id
        self.dynamicMap = DynamicMap()
        if not(dynamicMap is None):
            self.dynamicMap = dynamicMap

    # sensors : (3*3) string array sent by the world
    def sense_world(self, sensors):
        rad = sensors.shape[0]//2
        for x in range(sensors.shape[0]):
            for y in range(sensors.shape[1]):
                if sensors[x,y] != '':
                    self.dynamicMap.setVal((x-rad,y-rad), sensors[x,y])
        

    def move(self, possible_directions):
        if possible_directions == []:
            return None
        dir = rd.choice(possible_directions)
        self.dynamicMap.shift(dir)
        return dir