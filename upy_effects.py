import time


class NeoPixel_Effects:
    def __init__(self, pixel_strand):
        self.pixels = pixel_strand
        self.numpix = len(pixel_strand)

    def rainbow(self, wait_time):
        for j in range(256):
            for i in range(self.numpix):
                self.pixels[i] = self.Wheel((i + j) & 255)
            self.pixels.write()
            self.delay(wait_time)

    def rainbowCycle(self, wait_time, cycles):
        for j in range(256 * cycles):
            for i in range(self.numpix):
                self.pixels[i] = self.Wheel((int(i * 256 / self.numpix) + j) & 255)
            self.pixels.write()
            self.delay(wait_time)

    def colorWipe(self, color, wait_time):
        for pixel in range(self.numpix):
            self.pixels[pixel] = color
            self.pixels.write()
            self.delay(wait_time)

    def Wheel(self, WheelPos):
        WheelPos = 255 - WheelPos
        if WheelPos < 85:
            return (255 - WheelPos * 3, 0, WheelPos * 3)
        if WheelPos < 170:
            WheelPos -= 85
            return (0, WheelPos * 3, 255 - WheelPos * 3)
        WheelPos -= 170
        return (WheelPos * 3, 255 - WheelPos * 3, 0)

    def delay(self, ms):
        time.sleep(ms / 1000)
