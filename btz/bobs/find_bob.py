import pyautogui, time, keyboard, os
import numpy as np
import soundcard as sc

# Function to find the bobber in the game
def find_bob():
    global bob_found
    # Get the current working directory
    current_dir = os.getcwd()
    # Define the directory where the bobber images are stored
    bob_directory = "C:\\Users\\darcy\Desktop\\bobs"

    while True:
        print("<< Looking for Bob. Hold esc to quit. >>")
        bob_found = False
        # Sleep for a random time between 1.3 and 1.7 seconds
        time.sleep(np.random.uniform(1.3,1.7))

        # If the escape key is pressed, exit the program
        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()

        try:
            # Loop through all the files in the bobber directory
            for file in os.listdir(bob_directory):
                # If the file is a jpg image
                if file.endswith(".jpg"):
                    file = (f"{bob_directory}/{file}")
                    # Try to find the image on the screen
                    screen_loc = pyautogui.locateOnScreen(file, confidence=0.8, grayscale=True)
                    # If the image is found
                    if screen_loc:
                        print("<< Bob identified. >>")
                        # Calculate the location to move the mouse to
                        screen_loc_offset = ((screen_loc[0] + int(screen_loc[2] / 2) + np.random.uniform(-3,3)), (screen_loc[1] + int(screen_loc[3] / 2)) + np.random.uniform(-3,3))
                        print("<< Moving to bob... >>")
                        # Move the mouse to the calculated location
                        pyautogui.moveTo(screen_loc_offset[0], screen_loc_offset[1], np.random.uniform(0.4,1.1), pyautogui.easeOutQuad)
                        bob_found = True
                        break
        except pyautogui.ImageNotFoundException:
            pass
        break

find_bob()