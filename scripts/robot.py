import numpy as np
import random as rd
from enum import Enum, auto
from scripts.dynamicmap import DynamicMap, Dir

class Robot:

    def __init__(self, dynamicMap=None):
        self.dynamicMap = DynamicMap()
        if not(dynamicMap is None):
            self.dynamicMap = dynamicMap

    # sensors : (3*3) string array sent by the world
    def update_dynamicMap(self, sensors):
        for x in range(-1,2):
            for y in range(-1,2):
                self.dynamicMap.setVal((x,y), sensors[x,y])

    def dectect_friend(self):
        print("pouet")
    
    def moving(self):
        dir = rd.choice(list(Dir))
        


print("Hello")