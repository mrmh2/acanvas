import numpy as np
import scipy.misc
from coords2d import Coords2D

class Canvas(object):

    def __init__(self, xdim, ydim):
        self.array = np.zeros((xdim, ydim, 3), dtype=np.uint8)

    def save_as_png(self, filename):
        scipy.misc.imsave(filename, self.array)

    def __setitem__(self, key, value):
        self.array[key] = value

    def draw_line(self, p1, p2):
        delta = p2 - p1
        length = abs(delta)
        norm_grad = delta / length

        for i in range(0, 1+int(length)):
            p = p1 + norm_grad * i
            self.array[p.astuple()] = (255, 255, 255)

class Quad(object):

    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def draw(self, canvas):
        canvas.draw_line(self.p1, self.p2)
        canvas.draw_line(self.p2, self.p3)
        canvas.draw_line(self.p3, self.p4)
        canvas.draw_line(self.p4, self.p1)

def main():
    canvas = Canvas(500, 500)

    canvas[50, 50] = (255, 255, 255)

    p1 = Coords2D(100, 100)
    p2 = Coords2D(100, 300)
    p3 = Coords2D(300, 300)
    p4 = Coords2D(100, 300)

    rect = Quad(p1, p2, p3, p4)
    rect.draw(canvas)

    canvas.save_as_png('test.png')

if __name__ == '__main__':
    main()
