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
    for i in range(5):
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
    sleep(randint(0, 60))
