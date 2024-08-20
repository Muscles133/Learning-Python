import pyautogui, time, keyboard, os
import numpy as np
import soundcard as sc
import win32api, win32con
import random

from hear_bob import hear_bob
from find_bob import find_bob
#from check_bait import check_bait


def main():
    ammount = 0
    while keyboard.is_pressed ('q') == False:

        bob = False
        sound = False
        
        press_8() # cast the line

        time.sleep(np.random.uniform(1, 2)) #random sleep # Sleep a little before moving to curser


        if find_bob():

            while True:  # Outer loop to keep the program running
                start_time = time.time()
                sound_heard = False

                while not sound_heard:
                    if time.time() - start_time > 16:
                        print("Didn't Hear Anything!")
                        break  # Exit the inner loop after 16 seconds

                    try:
                        if hear_bob():
                            click()  # collect fish
                            ammount += 1
                            time.sleep(np.random.uniform(0.5, 2))  # random sleep
                            print("Fish Caught!")
                            sound_heard = True
                        else:
                            time.sleep(np.random.uniform(0.1, 0.3))  # random sleep

                    except Exception as e:
                        print(f"An error occurred: {e}")
                        time.sleep(1)  # Wait a bit before retrying

                print(f"Total fish caught: {ammount}")
                break
                # The outer loop will restart here, effectively resetting everything



        else:
            pass


    # check bait
 

def click():
    win32api.mouse_event (win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(np.random.uniform(0.1, 0.3)) #random sleep
    win32api.mouse_event (win32con.MOUSEEVENTF_RIGHTUP,0,0)

def press_8():
    print("Casting Line!")
    pyautogui.keyDown('8')
    time.sleep(np.random.uniform(0.1, 0.3)) #random sleep
    pyautogui.keyUp('8')
    time.sleep(np.random.uniform(0.1, 0.3)) #random sleep


if __name__ == "__main__":
    main()