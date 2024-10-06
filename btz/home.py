import pyautogui
import keyboard
import sys
import time
import random
import numpy as np


def main():  # main fishing loop
    time.sleep(2)

    loc_1 = (3438, 451)
    loc_2 = (3480, 1674)

    while keyboard.is_pressed("q") == False:
        pyautogui.leftClick(loc_1[0], loc_1[1], duration=0.5)

        time.sleep(5)

        pyautogui.keyDown("w")
        time.sleep(np.random.uniform(0.1, 0.3))
        pyautogui.keyUp("w")  # add a sleep after this (1)

        pyautogui.leftClick(loc_2[0], loc_2[1], duration=0.5)


if __name__ == "__main__":
    main()