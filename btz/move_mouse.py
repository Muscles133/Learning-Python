

import pyautogui
import cv2
import numpy as np
import time

def calculate_centroid(mask):
    # Calculate moments of the mask
    M = cv2.moments(mask)
    
    # Calculate centroid
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return (cX, cY)
    return None

def detect_red_motion_and_move_mouse():
    # Capture the initial screen
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    
    # Get the screen dimensions
    height, width = screen.shape[:2]
    
    prev_centroid = None
    cooldown = 0
    
    while True:
        try:
            # Capture the current screen
            current_screen = pyautogui.screenshot()
            current_screen = cv2.cvtColor(np.array(current_screen), cv2.COLOR_RGB2BGR)
            
            # Convert to HSV color space
            current_hsv = cv2.cvtColor(current_screen, cv2.COLOR_BGR2HSV)
            
            # Define range for red color and create a mask
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(current_hsv, lower_red, upper_red)
            
            lower_red = np.array([170, 120, 70])
            upper_red = np.array([180, 255, 255])
            mask2 = cv2.inRange(current_hsv, lower_red, upper_red)
            
            mask = mask1 + mask2
            
            # Calculate centroid of the red area
            centroid = calculate_centroid(mask)
            
            if centroid and cooldown == 0:
                # Check if the centroid has moved
                if prev_centroid is None or centroid != prev_centroid:
                    print(f"Red object detected at: {centroid}")
                    
                    # Move mouse to the centroid location
                    pyautogui.moveTo(centroid[0], centroid[1])
                    
                    prev_centroid = centroid
                    cooldown = 20  # Set a cooldown period
            else:
                if cooldown > 0:
                    cooldown -= 1
            
            # Small delay to reduce CPU usage
            time.sleep(0.1)
            
        except KeyboardInterrupt:
            print("Script stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    print("Red motion detection and mouse movement started. Press Ctrl+C to stop.")
    detect_red_motion_and_move_mouse()


