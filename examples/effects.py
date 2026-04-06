import machine
import time
import random
import neopixel
import gc
import colorsupport


def fill_spiral(pix, c, start, interval):
    n = len(pix)
    for i in range(0, n, interval):
        pix[(i + start) % n] = c


def update_fill(pix, c=(0, 20, 40), npix=120, start=0, dstart=1, interval=30):
    if not isinstance(c[0], (list, tuple)):
        c = [c]
    pix.fill((0, 0, 0))
    for cu in c:
        fill_spiral(pix, cu, start, interval)
        start = start + dstart


def dotest(
    nstep, pin=1, c=(0, 20, 40), npix=120, start=0, dstart=1, interval=30, tsleep=0.1
):
    pix = neopixel.NeoPixel(machine.Pin(pin), npix)
    stepstart = start
    while nstep := nstep - 1:
        update_fill(
            pix, c=c, npix=npix, start=stepstart, dstart=dstart, interval=interval
        )
        pix.write()
        stepstart = (stepstart + 2) % npix
        time.sleep(tsleep)


csimp = [(0, 20, 40), (30, 0, 10), (10, 50, 1)]
cbp = [(50, 0, 1), (50, 0, 1), (20, 20, 20), (20, 20, 20)]


def randomColor(bright):
    ci = random.randint(0, 255)
    return colorsupport.colorwheel(ci, bright=bright)


def dorandom(leds, nrandom=None, bright=1):
    if nrandom is not None and random.randint(0, 10) > 8:
        for _ in range(nrandom):
            rled = random.randint(0, len(leds) - 1)
            leds[rled] = randomColor(bright=bright)
        leds.write()
        gc.collect()


def update_leds(
    leds, doupdate, tdur_secs=60, step=1, dly=0.1, sclr=False, nrandom=None, bright=0.1
):
    tend = tdur_secs
    if tdur_secs is not None:
        tend = time.ticks_add(time.ticks_ms(), tend * 1000)
    i = 0
    llen = len(leds)
    print("loop_led_time: npix = ", llen)
    while tend is None or time.ticks_ms() < tend:
        doupdate(leds, start=i, clear=sclr)
        if nrandom is not None:
            dorandom(leds, nrandom=nrandom, bright=bright)
        if dly:
            time.sleep(dly)
        i = (i + step) % llen
        if i == 0 and tend is None:
            gc.collect()
    # offall(leds)
    gc.collect()


class Effects:
    def __init__(self, pix, update=None):
        self.pix = pix
        self.update = update

    def run(self):
        self.update()
