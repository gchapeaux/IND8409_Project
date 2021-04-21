import numpy as np
from enum import Enum, auto
from scripts.dynamicmap import DynamicMap, Dir

class Robot:

    def __init__(self, dynamicMap):
        self.dynamicMap = dynamicMap

    def update_dynamicMap(self,dynamicMap):
        print("pouet")

    def dectect_friend(self):
        print("pouet")


"""
    def reshape(self, newRadius):
        newMap = np.empty(shape=(2*newRadius+1, 2*newRadius+1), dtype=str)
        if newRadius >= self.RADIUS:
            oldmin, oldmax = -self.RADIUS, self.RADIUS
            self.RADIUS = newRadius
            newMap[self.__c2a(oldmin) : self.__c2a(oldmax)+1 , self.__c2a(oldmin) : self.__c2a(oldmax)+1] = self.map
            self.map = newMap
        else:
            newmin, newmax = -newRadius, newRadius
            self.map = self.map[self.__c2a(newmin) : self.__c2a(newmax) + 1, self.__c2a(newmin) : self.__c2a(newmax) + 1]
            self.RADIUS = newRadius

    def setVal(self, cc_elem, val):
        cx_elem, cy_elem = cc_elem[0], cc_elem[1]
        if max(abs(cx_elem), abs(cy_elem)) > self.RADIUS:
            self.reshape(max(abs(cx_elem), abs(cy_elem)))
        self.map[self.__c2a(cx_elem), self.__c2a(cy_elem)] = val

    def getVal(self, cc_elem):
        cx_elem, cy_elem = cc_elem[0], cc_elem[1]
        if max(abs(cx_elem), abs(cy_elem)) > self.RADIUS:
            self.reshape(max(abs(cx_elem), abs(cy_elem)))
        return self.map[self.__c2a(cx_elem), self.__c2a(cy_elem)]

    def shift(self, dir):
        if dir = Dir.NORTH:
            if not(np.all(e == '' for e in self.map[-1])):
                self.reshape(self.RADIUS+1)

"""



print("Hello")