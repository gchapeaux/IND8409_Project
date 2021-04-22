import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

ATLAS_INDEXES = {'' : 0, '@' : 1, '.' : 2, 'T' : 3, 'W' : 4, 'S' : 5, 'R' : 6, 'F' : 7}
indexing = np.vectorize(lambda s : ATLAS_INDEXES[s])

color_list = [(0.0,0.0,0.0), (0.3,0.3,0.3), (0.5,0.5,0.5), (0.0,0.3,0.0), (0.0,0.0,1.0),(0.2,0.2,1.0), (1.0,0.0,0.0), (0.90, 0.15, 0.30)]
ATLAS_COLORS = ListedColormap(color_list, name='colors', N=256)
ATLAS_NORM = BoundaryNorm([0,1,2,3,4,5,6,7], 7)

def read_map(path_to_map):
    map_mx = []
    with open(path_to_map) as mapfile:
        lines = mapfile.readlines()
    for line in lines[4:517]:
        map_line = list(line.replace('\n',''))
        map_mx.append(map_line)
    return np.array(map_mx)

def viz_map(map_mx, fig_name=None, save_path = None, show=True):
    fig, ax = plt.subplots()
    plt.imshow(indexing(map_mx), cmap=ATLAS_COLORS, norm=ATLAS_NORM)
    ax.set_axis_off()
    if not(fig_name is None):
        fig.suptitle(fig_name)
    if not(save_path is None):
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close(fig)

def viz_map_robot(robot, ax, radius):
    map_mx = robot.dynamicMap.map_extract(radius)
    ax.imshow(indexing(map_mx), cmap=ATLAS_COLORS, norm=ATLAS_NORM)

def viz_map_world(worldmap, ax):
    ax.imshow(indexing(worldmap), cmap=ATLAS_COLORS, norm=ATLAS_NORM)