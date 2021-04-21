import numpy as np
from enum import Enum, auto

class Dir(Enum):
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()
    EAST = auto()

class DynamicMap:

    def __init__(self, array=None):
        if array is None:
            self.map = np.empty(shape=(3,3), dtype=str)
        else:
            self.map = np.array(array, dtype=str)
        self.RADIUS = 1

    __c2a = lambda self, rc : rc+self.RADIUS # Centered to absolute coordinate
    __a2c = lambda self, ac : ac-self.RADIUS # Absolute to centered coordinate

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
        if dir == Dir.NORTH:
            if not(np.all(self.map[-1] == '')):
                self.reshape(self.RADIUS+1)
            self.map = np.concatenate((np.empty((1,2*self.RADIUS+1), dtype=str), self.map), axis=0)[:-1,:]
        elif dir == Dir.SOUTH:
            if not(np.all(self.map[0] == '')):
                self.reshape(self.RADIUS+1)
            self.map = np.concatenate((self.map, np.empty((1,2*self.RADIUS+1), dtype=str)), axis=0)[1:,:]
        elif dir == Dir.EAST:
            if not(np.all(self.map[:,0] == '')):
                self.reshape(self.RADIUS+1)
            self.map = np.concatenate((self.map, np.empty((2*self.RADIUS+1, 1), dtype=str)), axis=1)[:,1:]
        elif dir == Dir.WEST:
            if not(np.all(self.map[:,-1] == '')):
                self.reshape(self.RADIUS+1)
            self.map = np.concatenate((np.empty((2*self.RADIUS+1,1), dtype=str), self.map), axis=1)[:,:-1]

    def mergeMaps(self, received_map, cc): # cc for centered coordinates of the emitting robot
        

print("Hello")