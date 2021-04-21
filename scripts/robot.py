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
        for x in range(-1,2):
            for y in range(-1,2):
                if sensors[x+1,y+1] != '':
                    self.dynamicMap.setVal((x,y), sensors[x+1,y+1])
        

    def move(self, possible_directions):
        dir = rd.choice(possible_directions)
        self.dynamicMap.shift(dir)
        return dir


print("Hello")