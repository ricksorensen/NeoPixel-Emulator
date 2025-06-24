from upy_backend import NeoPixel
from neopixel_gfx import Adafruit_GFX
from time import sleep


class NeoMatrix(Adafruit_GFX):
    positions = {
        "NEO_MATRIX_TOP": 0,
        "NEO_MATRIX_BOTTOM": 1,
        "NEO_MATRIX_LEFT": 0,
        "NEO_MATRIX_RIGHT": 2,
        "NEO_MATRIX_CORNER": 3,
        "NEO_MATRIX_ROWS": 0,
        "NEO_MATRIX_COLUMNS": 4,
        "NEO_MATRIX_AXIS": 4,
        "NEO_MATRIX_PROGRESSIVE": 0,
        "NEO_MATRIX_ZIGZAG": 8,
        "NEO_MATRIX_SEQUENCE": 8,
    }

    def create_matrix(self, pin, width, height, pixsize=35):
        self.width = width
        self.height = height
        self.absoluteWidth = width
        self.absoluteHeight = height
        self.pin = pin
        self.pixels = NeoPixel(
            self.pin, self.width * self.height, pixsize=pixsize, init=False
        )
        self.pixsize = pixsize
        self.begin(width=width, height=height)

    def delay(self, ms):
        sleep(ms / 1000)

    def begin(self, width, height):
        needed_w = self.width * self.pixsize
        needed_h = self.height * (self.pixsize - 1) + 4
        self.pixels.begin(
            width=self.width,
            height=self.height,
            window_w=needed_w,
            window_h=needed_h,
        )

    def drawPixel(self, x, y, color):
        x, y = self.mapPixelToRotation(x, y)
        if x is None or y is None:
            pass
        else:
            self.pixels[y * self.width + x] = color

    def show(self):
        self.pixels.gui.render()
        _ = self.pixels.gui.dispatch_events()

    def setBrightness(self, new_brightness):  # use opacity to represent this
        if new_brightness >= 0 and new_brightness <= 100:
            self.brightness = new_brightness
            self.pixels.gui.change_brightness(self.brightness)
        else:
            return False


bitmap_array = [0x00, 0x84 >> 1, 0x84 >> 1, 0x00, 0x00, 0x84 >> 1, 0x78 >> 1, 0x00]

if __name__ == "__main__":
    matrix = NeoMatrix()
    matrix.create_matrix(
        6,
        15,
        10,
        pixsize=10,
    )
    # matrix.begin()
    matrix.show()
    matrix.setRotation(0)
    matrix.setBrightness(90)
    matrix.drawPixel(0, 0, (200, 12, 70))
    matrix.show()
    matrix.delay(2000)
    matrix.drawPixel(3, 2, (200, 12, 70))
    matrix.show()
    matrix.delay(2000)
    matrix.fillRect(0, 0, 4, 2, (200, 12, 70))
    matrix.show()
    matrix.delay(2000)
    matrix.fillScreen((200, 12, 70))
    matrix.show()
    matrix.delay(2000)
    matrix.fillCircle(5, 5, 3, (0, 0, 255))
    matrix.show()
    matrix.delay(2000)
    matrix.drawCircle(10, 10, 8, (0, 255, 0))
    matrix.show()
    matrix.delay(2000)
    matrix.fillRoundRect(0, 0, 10, 6, 3, (0, 50, 150))
    matrix.show()
    matrix.delay(2000)
    matrix.drawTriangle(0, 0, 9, 2, 4, 9, (160, 160, 0))
    matrix.show()
    matrix.delay(2000)
    # matrix.clearScreen()
    matrix.drawBitmap(
        0, 0, bitmap_array, 8, 8, (0, 0, 0), background_color=(200, 200, 200)
    )
    matrix.show()
    matrix.delay(3000)
