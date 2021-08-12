from pynput.keyboard import Key, Controller
from time import sleep
from random import randint

keyboard = Controller()
ctrl = Key.tab
alt  = Key.alt

while True:
    try:
        keyboard.press(Key.page_down)
        sleep(1)
        keyboard.release(Key.page_down)
    except Exception as e:
        print(e)
    sleep(randint(40, 90))
    try:
        keyboard.press(Key.page_down)
        sleep(1)
        keyboard.release(Key.page_down)
    except Exception as e:
        print(e)
    sleep(randint(40, 90))
    try:
        keyboard.press(Key.page_down)
        sleep(1)
        keyboard.release(Key.page_down)
    except Exception as e:
        print(e)
    sleep(randint(40, 90))
    try:
        keyboard.press(Key.page_down)
        sleep(1)
        keyboard.release(Key.page_down)
    except Exception as e:
        print(e)
    sleep(randint(40, 90))
    keyboard.press(ctrl)
    keyboard.press(alt)
    sleep(3)
    keyboard.release(alt)
    keyboard.release(ctrl)
    sleep(3)
    sleep(randint(120, 180))
    try:
        keyboard.press(Key.page_down)
        sleep(1)
        keyboard.release(Key.page_down)
    except Exception as e:
        print(e)
    sleep(randint(0, 60))
