from pixel import Pixel
from neopixel_emulator import NeoPixel_Emulator


class NeoPixel:
    def __init__(self, pixel_pin, pixel_num, window_w=1765, window_h=400, pixsize=35):
        self.pixel_number = pixel_num
        self.pin = pixel_pin
        self.brightness = 100
        self.pixsize = pixsize
        self.started = False

    def begin(self, width=None, height=None, window_w=1765, window_h=400):
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

    def __len__(self):
        return self.pixel_number

    def __setitem__(self, i, v):
        self.gui.draw_color(i, v)
        self.pixel_list[i].update_color(v)

    def __getitem__(self, i):
        return self.pixel_list[i].get_color()

    def write(self):
        # for pixel in self.pixel_list:
        # print("Pixel {0} has color {1}".format(pixel.get_position(),pixel.get_color()))
        self.gui.render()

    def fill(self, v):
        for i in range(0, self.pixel_number):
            self.gui.draw_color(i, v)
            self.pixel_list[i].update_color(v)

    def fclose(self):
        self.gui.close()
