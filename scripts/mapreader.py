import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

map_colors = {
    '@' : (0,0,0),
    '.' : (150,150,150),
    'T' : (0,255,0),
    'W' : (0,0,255),
    'S' : (50,50,255)
}
plt.register_cmap(cmap=LinearSegmentedColormap('MapColors', map_colors))

def read_map(path_to_map):
    map_mx = []
    with open(path_to_map) as mapfile:
        lines = mapfile.readlines()
    for line in lines[4:517]:
        map_line = line.split()
        map_mx.append(map_line)
    return map_mx

def viz_map(map_mx, colors=map_colors):
    plt.imshow(map_mx, cmap=plt.get_cmap('MapColors'))
    plt.show()

test = read_map('data/losttemple.map')
viz_map(test)