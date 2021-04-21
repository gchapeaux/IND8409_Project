import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

ATLAS_INDEXES = {'@' : 0, '.' : 1, 'T' : 2, 'W' : 3, 'S' : 4}
indexing = np.vectorize(lambda s : ATLAS_INDEXES[s])

color_list = [(0.0,0.0,0.0), (0.5,0.5,0.5), (0.0,0.3,0.0), (0.0,0.0,1.0),(0.2,0.2,1.0)]
ATLAS_COLORS = ListedColormap(color_list, name='colors', N=256)
ATLAS_NORM = BoundaryNorm([0,1,2,3,4], 4)

def read_map(path_to_map):
    map_mx = []
    with open(path_to_map) as mapfile:
        lines = mapfile.readlines()
    for line in lines[4:517]:
        map_line = list(line.replace('\n',''))
        map_mx.append(map_line)
    return np.array(map_mx)

def viz_map(map_mx):
    plt.imshow(indexing(map_mx), cmap=ATLAS_COLORS, norm=ATLAS_NORM)
    plt.show()

print("Hello")