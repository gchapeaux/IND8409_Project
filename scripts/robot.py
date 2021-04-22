import numpy as np
import random as rd
from enum import Enum, auto
from scripts.dynamicmap import DynamicMap, Dir

class Robot:

    __NEW_BEHAVIOUR_CHANCE = 0.1

    def __init__(self, id, dynamicMap=None):
        self.id = id
        self.dynamicMap = DynamicMap()
        if not(dynamicMap is None):
            self.dynamicMap = dynamicMap
        self.pref_dir = Dir(id%4)
        self.exploration_history = []

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
        roll = rd.random()
        if (roll < self.__NEW_BEHAVIOUR_CHANCE or self.pref_dir not in possible_directions):
            self.pref_dir = rd.choice(possible_directions)
        self.dynamicMap.shift(self.pref_dir)
        self.dynamicMap.map_opti()
        return self.pref_dir

    def mergeMaps(self, map, coords):
        self.dynamicMap.mergeMaps(map, coords)
        #self.dynamicMap.mergeApproximateMaps(map, coords)
        self.dynamicMap.map_opti()

    def write_history(self):
        self.exploration_history.append(np.sum(self.dynamicMap.map != ''))