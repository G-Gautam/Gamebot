from PIL import ImageGrab
import os
import time
from ctypes import windll


user32 = windll.user32
user32.SetProcessDPIAware()


def screenGrab():
    box = (510, 447, 1789, 1406)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()