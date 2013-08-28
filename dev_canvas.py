from acanvas.acanvas import Canvas
from coords2d import Coords2D

def main():

    c = Canvas(500, 500)
    p1 = Coords2D(10, 10)
    p2 = Coords2D(110, 110)
    c.rect(p1, p2)
    c.save_as_png("test.png")

if __name__ == '__main__':
    main()
