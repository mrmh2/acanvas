from acanvas.acanvas import Canvas
from acanvas.coords2d import Coords2D
from acanvas.fonty import Font

def main():

    c = Canvas(800, 500)
    p1 = Coords2D(10, 10)
    p2 = Coords2D(110, 110)
    c.rect(p1, p2)

    c.draw_text( Coords2D(200, 200), 'Here is some text!' , font='fonts/UbuntuMono-R.ttf')

    c.save_as_png("test.png")


if __name__ == '__main__':
    main()
