# NeoPixel-Emulator
NeoPixel Emulator in Python with Pyglet

This emulator has two main ways to emulate. One is a simple NeoPixel strip with the basic setPixelColor and some simple effects, and the other is a matrix emulator. You can create large matrices that dynamically resize the window based on the size. There is also an almost one-to-one port of the Adafruit GFX library, which allows for the creation of many graphics primitives and even the drawing of monochrome bitmaps from an array. The only thing not implemented is tiling and printing of text.

## requirements

  + pyglet (e.g. from `pypi`)

## modules

  * `emulator_backend`:  emulate the `circuitpython` `neopixel`  API  (see `neopixel_emulator` for LED emulation)
  * `pixel`: simple class to hold pixel information 
  * `neopixel_emulator`: emulate the `neopixel` LED strip activation with `pyglet`
  * `neopixel_effects`: drive effects into LED strip, `circuitpython` dependent independent emulator of LED hardware
  * `neopixel_gfx`: special effects, independent of emulator/hardware

  * `neopixel_viewer`: demonstration 
  * `neopixel_neomatrix`: demonstration

		
# micropython NeoPixel

NeoPixel class emulator in CPython with Pyglet for `micropython` `neopixel` class.

  *  `upy_backend`:  emulate the `micropython` `neopixel`  API  (see `neopixel_emulator` for LED emulation)
  * `upy_effects`: drive effects into LED strip, `micropython` dependent  emulator of LED hardware
  *  `led_panel`: demonstration class
  *  `rjstext`: demonstration drive led_panel
  *  `upy_viewer`: demonstration
  *  `upy_matrix`: demonstration

		
