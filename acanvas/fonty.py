import freetype

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

    @staticmethod
    def unpack_mono_bitmap(bitmap):
        """Unpack a freetype FT_LOAD_TARGET_MONO glyph bitmap into a bytearray 
        where each pixel is represented as a single byte."""

        data = bytearray(bitmap.rows * bitmap.width)

        # Iterate over packed byted in the input bitmap
        for y in range(bitmap.rows):
            for byte_index in range(bitmap.pitch):
                
                # Read byte with packed pixel data
                byte_value = bitmap.buffer[y * bitmap.pitch + byte_index]

                # Update how many bits we've processed
                num_bits_done = byte_index * 8

                # Work out where to write pixels we're going to unpack
                rowstart = y * bitmap.width + byte_index * 8

                # Iterate over each bit that's part of the output bitmap
                for bit_index in range(min(8, bitmap.width - num_bits_done)):
                    
                    # Unpack next pixel
                    bit = byte_value & (1 << (7 - bit_index))

                    # Write pixel to output bytearray
                    data[rowstart + bit_index] = 1 if bit else 0

        return data
    
class Bitmap(object):
    """2D bitmap image as list of byte values."""

    def __init__(self, width, height, pixels=None):
        self.width = width
        self.height = height
        self.pixels = pixels or bytearray(width * height)

    def __repr__(self):
        """String representation of bitmap's pixels."""
        rows = ''
        for y in range(self.height):
            for x in range(self.width):
                rows += '*' if self.pixels[y * self.width + x] else ' '
            rows += '\n'

        return rows
