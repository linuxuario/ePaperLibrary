# ePaperLibrary for Waveshare e-Paper Raspberry HAT

Simple library to use the [Waveshare 2.7inch e-Paper HAT](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT).

This ePaper hat is cheap compared to the PaPiRus e-Paper hat. The only problem is that this device hasn't simple library, so hello there.



**Features**:

- Use screen in Landscape or Portrait
- Write simple texts
- Add ligne
- Not physical refresh if same image




**ToDo**:

- Show the calculated image when you don't have the Hat available *Soon*
- Add images

  ​



## Installation

W.I.P



## Usage (main.py)

```python
import epsimplelib

def hello_world():
	esp = epsimplelib.EPScreen('landscape') # eps = e-Ink Paper Screen
	esp.set_title("Hello world")

	esp.add_line((132, 70, 92, 135))
	esp.add_line((92, 135, 172, 135))
	esp.add_line((172, 135, 132, 70))

	esp.update_screen()

hello_world()
hello_world() # Physical screen not refreshed if it is the same
```



## Ressources

- The library uses the Original Library written by Waveshare. It can be [downloaded here](https://www.waveshare.com/wiki/File:2.7inch-e-paper-hat-code.7z). Modified to run on Python3
- FreeMonoBold by GNU FreeFont



## Author

- Nicolas SAGOT - @Lyoko17220




## Licence

MIT. See [LICENCE.md](LICENCE.md)
