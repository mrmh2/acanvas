import numpy as np
import scipy.misc

from coords2d import Coords2D

class Canvas(object):

    def __init__(self, x_size, y_size):
        self.dim = x_size, y_size

        self.array = np.zeros((x_size, y_size, 3), dtype=np.uint8)

    def save_as_png(self, filename):
        scipy.misc.imsave(filename, self.array)

    def __setitem__(self, key, value):
        self.array[key] = value

    def rect(self, p1, p2, col=(255, 255, 255)):
        
        for x in range(p1.x, p2.x + 1):
            for y in range(p1.y, p2.y + 1):
                self.array[x, y] = col
