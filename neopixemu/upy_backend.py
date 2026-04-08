"""
MicroPython NeoPixel Strip emulation.
"""

from .pixel import Pixel
from .neopixel_emulator import NeoPixel_Emulator


class machine:
    """Dummy partial implementation of MicroPython machine class.

    For this emulation it implements a `machine.Pin()` class interface.
       machine.Pin()
    """

    class Pin:
        """Dummy partial Pin class.

        Parameter
        ---------

        pref int : Pin (gpio) number
        """

        def __init__(self, pref: int):
            self.p = pref

    def _init_(self):
        pass


class NeoPixel:
    """Emulated MicroPython neopixel.NeoPixel class

    Parameter
    ---------
    pixel_pin:  Gpio (pin) number.
    pixel_num:  Number of pixels in strip.
    init:       optional whether or not to start emulation display now
    window_w:   optional Size of neopixel emulation window
    window_h:   optional
    pixsize:    optional Size of pixel
    """

    def __init__(
        self,
        pixel_pin: int,
        pixel_num: int,
        init: bool = True,
        window_w: int = 1765,
        window_h: int = 400,
        pixsize: int = 10,
    ):
        self.pixel_number = pixel_num
        self.pin = pixel_pin
        self.brightness = 100
        self.pixsize = pixsize
        self.started = False
        if init:
            self.begin(window_w=window_w, window_h=window_h)

    def begin(self, width=None, height=None, window_w=1765, window_h=400) -> None:
        """Start emulated display.

        Starts NeoPixel_Emulator and builds up data structures.

        Args:
            width: screen width of emulated display
            height: screen height of emulated display
            window_w: tbd
            window_h: tbd
        """
        self.gui = NeoPixel_Emulator(
            window_w=window_w, window_h=window_h, pixsize=self.pixsize
        )
        self.pixel_list = list()
        for pixel in range(self.pixel_number):
            self.pixel_list.append(Pixel(pixel))
        if width is not None and height is not None:
            self.gui.draw_LED_matrix(width, height)
        else:
            self.gui.draw_LEDs(self.pixel_number)
        self.gui.render()
        self.started = True

    def __len__(self) -> int:
        return self.pixel_number

    def __setitem__(self, i: int, v: tuple[int, int, int]):
        self.gui.draw_color(i, v)
        self.pixel_list[i].update_color(v)

    def __getitem__(self, i: int):
        return self.pixel_list[i].get_color()

    def write(self):
        """Write data to emulated display."""
        # for pixel in self.pixel_list:
        # print("Pixel {0} has color {1}".format(pixel.get_position(),pixel.get_color()))
        self.gui.render()

    def fill(self, v: tuple[int, int, int]):
        """Fill emulated display with same color.

        Args:
            v: R,G,B tuple
        """
        for i in range(0, self.pixel_number):
            self.gui.draw_color(i, v)
            self.pixel_list[i].update_color(v)

    def fclose(self):
        """Close pyglet display."""
        self.gui.close()
