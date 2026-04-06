# NeoPixel-Emulator
NeoPixel Emulator in Python with Pyglet

This emulator has two main ways to emulate. One is a simple NeoPixel strip with the basic setPixelColor and some simple effects, and the other is a matrix emulator. You can create large matrices that dynamically resize the window based on the size. There is also an almost one-to-one port of the Adafruit GFX library, which allows for the creation of many graphics primitives and even the drawing of monochrome bitmaps from an array. The only thing not implemented is tiling and printing of text.

## requirements

  + pyglet (e.g. from `pypi`)

## modules

Here be original circuitpython modules.

  * `emulator_backend`:  emulate the `circuitpython` `neopixel`  API  (see `neopixel_emulator` for LED emulation)
  * `pixel`: simple class to hold pixel information 
  * `neopixel_emulator`: emulate the `neopixel` LED strip activation with `pyglet`
  * `neopixel_effects`: drive effects into LED strip, `circuitpython` dependent independent emulator of LED hardware
  * `neopixel_gfx`: special effects, independent of emulator/hardware
  * `neopixel_viewer`: demonstration 
  * `neopixel_neomatrix`: demonstration

## MicroPython modules

Since micropython and circuitpython  neopixel classes have different methods for pixel access, modules for micropython have been created.  NeoPixel class emulator in CPython with Pyglet for `micropython` `neopixel` class.  New modules are:

  * `upy_backend`:  emulate the `micropython` `neopixel`  API  (see `neopixel_emulator` for LED emulation)
  * `upy_effects`: drive effects into LED strip, `micropython` dependent  emulator of LED hardware replaces `neopixel_effects`

Examples are:

  * `led_panel`: demonstration class with effects derived from <https://github.com/MikeEllis-personal/DMXfire.git>
  * `rjstest`: demonstration drive led_panel
  * `upy_viewer`: demonstration (examples)
  * `upy_matrix`: demonstration
  * `effects`: unused

Reused modules:

* `neopixel_emulator`: used by `upy_backend`
  - clean up for new pyglet version.
  - can change pixel size.
  - set numpixels/row for linear strip.
* `neopixel_gfx`: only code clean up (ruff) used by examples
* `pixel`: only code clean up (ruff)




## Usage: With pyglet in your python path (e.g. venv):

The template for using the emulator or the actual hardware:

```
_real_hardware = False
try:
    from neopixel import NeoPixel
    import machine

    _realhardware = True
except ModuleNotFoundError:
    from upy_backend import NeoPixel
    from upy_backend import machine

```
then use as normal.  Remember for initializing the NeoPixel array the pin number is critical for real hardware but insignificant for the emulator. The emulator also has some optional additional parameters to defined the display on linux:
```
if _real_hardware:
	pixels = NeoPixel(ledPin, numberPixels)
else:
	pixels = NeoPixel(ledPin, numberPixels, init=True, window_w=1785, window_h=400,pixsize=10)
```
add at the end:
```
if not _real_hardware:
	pixels.fclose()      # ends pyglet session and closes display
```

See `examples/upy_viewer.py` and `example/led_panel.py`.

## Examples

These examples assume:

+ pyglet is available
+ in the repository home directory

For MicroPython:

+ run with the home directory mounted:
```
>mpremote mount .   # connects to hardware and makes current directory accessible
```
+ download the required modules to device.  Note that the upy_* modules are not necessary.
```
>mpremote mkdir :examples
>mpremote cp examples/*.py :examples    # copy examples to device
```

### From CPython:
```
python -m examples.upy_viewer
python -m examples.upy_matrix
python -m examples.rjstest      # uses led_panel
```

### from iPython:
```
import examples.upy_viewer
import examples.rjstest as rt   # uses led_panel
rt.fire_test()
```

### From MicroPython:

Interactive from REPL

```
import examples.upy_viewer
import examples.rjstest as rt
rt.fire_test()
```
