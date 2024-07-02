"""
This is my fishing bot 

"""

# checks for bait
# apply bait if missing
# dont look for bait if we dont have anything

# cast fishing pole
#confirm that the bob is in the correct position
# if not cast again

#wait for the splash *maybe listen to the splash?
# catch the fish
# timer on cast if nothing after X time recast
# check if bags are full or not

#log out if bags are full

# create a log that counts successfull catches
# log recasts and non catches

# hot key to start and stop


"""

    pyautogui.leftClick(1183, 629, duration = 0.5)
    pyautogui.hotkey("altleft", "f")
    time.sleep(0.5)
    pyautogui.typewrite("e")

"""


from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32, win32con
import psutil


def main(): # main fishing loop
    cast = 
    

    time.sleep(2)

    while keyboard.is_pressed("q") == False:

  




def check_bait(): # applies bait after a set amount of time.



def no_bait(): # exit the bot when there is not bait. set bait parameter.


def cast_rod(): # casts the line
    pyautogui.keyDown("8")
    time.sleep (np.random.uniform(0.1,0.3))
    pyautogui.keyUp ("8") #add a sleep after this (1)


def r_click(x,y): # right click
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(np.random.uniform(0.1,0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)


def l_click(x,y): # left click
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(0.1,0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)




# def kill_process(name):
#     for proc in psutil.process_iter():
#         if proc.name() == name:
#             proc.kill()




main()

# check if the q key is being pressed
while keyboard.is_pressed("q") == False:


#ensure a good sleep for auto loot to complete