# ScreenAverageColor
 Get the screen average color in python

### Dependencies
This program is written in Python 3.

- Pillow
- pyautogui

You can both install them via **`PIP`**
> `pip install Pillow`

> `pip install pyautogui`

### Usage
You just need to launch the script `average_screen_color.py`

You may get a warning but it should work.

Instead of double clicking the script (which could not work if you are on macOS for example), I recommend you opening your terminal/command prompt in the script's folder (you can use the command cd <path to the folder where the script is> to go to the script folder on UNIX-based system (i.e. macOS or Linux)).
 
 Then you should be able to do `python3 average_screen_color.py` to run the script.
 
 
### Commands/Arguments

While opening the script (`python3 average_screen_color.py`), you can pass it an option a number: the refresh rate.

This refresh rate determines the number of times a block of color is added before refreshing the window (Setting this number too high will result in a performance decrease).

For example: `python3 average_screen_color.py 15`.
