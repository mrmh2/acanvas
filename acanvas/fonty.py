class Font(object):
    """See:
    http://dbader.org/blog/monochrome-font-rendering-with-freetype-and-python"""

    def __init__(self, filename, size):
        self.face = freetype.Face(filename)
        self.face.set_pixel_sizes(0, size)

    def glyph_for_character(self, char):
        self.face.load_char(char, freetype.FT_LOAD_RENDER |
                            freetype.FT_LOAD_TARGET_MONO)
        return Glyph.from_glyphslot(self.face.glyph)
        
    def render_character(self, char):
        glyph = self.glyph_for_character(char)
        return glyph.bitmap

class Glyph(object):

    def __init__(self, pixels, width, height):
        self.bitmap = Bitmap(width, height, pixels)

    @staticmethod
    def from_glyphslot(slot):
        pixels = Glyph.unpack_mono_bitmap(slot.bitmap)
        width, height = slot.bitmap.width, slot.bitmap.rows
        return Glyph(pixels, width, height)
        
