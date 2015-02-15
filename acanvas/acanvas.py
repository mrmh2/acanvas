import os.path as _osp

import numpy as np
import scipy.misc

from fonty import Glyph, Font, Bitmap
from coords2d import Coords2D

class Canvas(object):

    def __init__(self, x_size, y_size):
        self.dim = x_size, y_size

        self.array = np.zeros((x_size, y_size, 3), dtype=np.uint8)

    def save_as_png(self, filename):
        scipy.misc.imsave(filename, np.transpose(self.array))

    def __setitem__(self, key, value):
        self.array[key] = value

    def rect(self, p1, p2, col=(255, 255, 255)):
        
        for x in range(p1.x, p2.x + 1):
            for y in range(p1.y, p2.y + 1):
                self.array[x, y] = col

    def draw_text(self, p, text, font="fonts/FreeMono.ttf", fsize=24):

        pkg_dir, name = _osp.split(_osp.abspath(__file__))

        font_path = _osp.join(pkg_dir, font)

        x_offset = p.x
        y_offset = p.y

        fnt = Font(font_path, fsize)
        ch = fnt.render_text(text)
        for y in range(ch.height):
            for x in range(ch.width):
                if ch.pixels[y * ch.width + x]:
                    self.array[x_offset + x, y_offset + y] = (255, 255, 255)

    # def draw_text(self, p, text, font="fonts/FreeMono.ttf", fsize=24):

    #     for char in text:
    #         self.draw_char(p, char, font, fsize)
    #         p += Coords2D(10, 0)


