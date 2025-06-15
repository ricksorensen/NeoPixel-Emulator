try:
    from neopixel import NeoPixel
    from machine import Pin
except ModuleNotFoundError:
    from upy_backend import NeoPixel

    def Pin(x):
        return x


from upy_effects import NeoPixel_Effects
import time


def mydelay(ms):
    time.sleep(ms / 1000)


def run():
    pixels = NeoPixel(Pin(2), 51)  # pixsize=10
    # pixels.begin()
    effects = NeoPixel_Effects(pixels)
    pixels[2] = (255, 200, 10)
    pixels.write()
    mydelay(200)
    pixels.fill((150, 60, 10))
    pixels.write()
    mydelay(1000)
    pixels.fill((0, 0, 0))
    effects.colorWipe((200, 12, 70), 50)
    pixels.fill((0, 0, 0))
    pixels.write()
    mydelay(1000)
    for i in range(5):
        effects.colorWipe((200, 0, 200), 10)
        pixels.fill((0, 0, 0))
    effects.rainbow(20)
    effects.colorWipe((150, 150, 0), 40)
    effects.rainbowCycle(20, 2)


run()
