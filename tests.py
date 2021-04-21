import numpy as np
from scripts.dynamicmap import DynamicMap

map = DynamicMap([['@','@','T'],['W','T','T'],['W','W','W']])
map2 = DynamicMap([['1','2','3'],['4','5','6'],['7','8','9']])
map.mergeMaps(map2, (-1,-1))

print(map.map)