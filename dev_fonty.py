from acanvas.fonty import *

def main():
    fnt = Font("acanvas/fonts/FreeMono.ttf", 24)
    ch = fnt.render_character("p")

    print ch

    txt = fnt.render_text("hello")

    print txt


if __name__ == '__main__':
    main()
