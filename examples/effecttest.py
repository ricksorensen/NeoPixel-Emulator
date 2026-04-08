from .effect_panel import effect_panel  # insist on using local module
import gc

brightness = 0
red = 1
green = 2
blue = 3
fade = 4
speed = 5


def beacon_test(
    ledPin=1, width=30, height=4, speed=128, stripe=10, brightness=255, nrun=100
):
    # Initialise the firelight effect
    panel = effect_panel(pin=ledPin, width=width, height=height)
    print(panel)

    for _ in range(nrun):
        panel.beacon(
            brightness=brightness,
            red=255,
            green=64,
            blue=10,
            speed=speed,
            stripe=stripe,
        )
        panel.update()

    panel.fill()
    panel.update()
    print("Finished")
    panel.fclose()


#  width=30, height=10, speed=80. brightness=80
def fire_test(
    ledPin=1,
    width=30,
    height=4,
    ledblock=10,
    speed=128,
    brightness=255,
    fade=255,
    nrun=100,
    debug=False,
):
    # Initialise the firelight effect
    panel = effect_panel(pin=ledPin, width=width, height=height, ledblock=ledblock)
    print(panel)
    for _ in range(nrun):
        # print(f"gcfree start: {gc.mem_free()}")
        panel.firelight(
            brightness=brightness,
            red=255,
            green=64,
            blue=10,
            speed=speed,
            fade=fade,
            debug=debug,
        )
        panel.update()
        # print(f"gcfree end: {gc.mem_free()}")
        gc.collect()

    panel.fill()
    panel.update()
    print("Finished")
    panel.fclose()


def strobe_test(
    ledPin=1, width=30, height=4, speed1=10, speed2=20, brightness=255, nrun=100
):
    # Initialise the firelight effect
    panel = effect_panel(pin=ledPin, width=width, height=height)
    print(panel)

    for _ in range(100):
        panel.strobe(
            brightness=brightness,
            red=255,
            green=64,
            blue=10,
            speed1=speed1,
            speed2=speed2,
        )
        panel.update()

    panel.fill()
    panel.update()
    print("Finished")
    panel.fclose()


def fourth_test(
    ledPin=1,
    npix=120,
    width=30,
    height=4,
    ledblock=10,
    speed=128,
    brightness=255,
    fade=255,
    nrun=100,
    flag=False,
    debug=False,
    top=True,
):
    # Initialise the firelight effect
    panel = effect_panel(
        pin=ledPin,
        width=width,
        height=height,
        ledblock=ledblock,
    )
    print(panel)
    for _ in range(nrun):
        # print(f"gcfree start: {gc.mem_free()}")
        panel.firelight(
            brightness=brightness,
            red=255,
            green=64,
            blue=10,
            speed=speed,
            fade=fade,
            debug=debug,
            top=top,
        )
        if flag:
            panel.flag(brightness=brightness, top=not top)
        panel.update()
        # print(f"gcfree end: {gc.mem_free()}")
        gc.collect()
    panel.fill()
    panel.update()
    print("Finished")
    panel.fclose()


def flag_test(
    ledPin=1,
    npix=120,
    size=24,
    niter=2,
    brightness=255,
    nrun=100,
    debug=False,
):
    # Initialise the firelight effect
    panel = effect_panel(ledPin, width=npix, height=1)
    print(panel)
    for _ in range(nrun):
        # print(f"gcfree start: {gc.mem_free()}")
        panel.flag(
            size=size,
            niter=niter,
            brightness=brightness,
        )
        panel.update()
        # print(f"gcfree end: {gc.mem_free()}")
        gc.collect()
    panel.fill()
    panel.update()
    print("Finished")
    panel.fclose()


if __name__ == "__main__":
    fourth_test(flag=False)
    fourth_test(flag=True)
    flag_test()
