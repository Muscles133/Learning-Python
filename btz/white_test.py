import cv2
import numpy as np
from PIL import ImageGrab
import time
import keyboard

# Get the screen size
screen_width, screen_height = ImageGrab.grab().size

# Define the area to capture (whole screen in this case)
capture_area = (0, 0, screen_width, screen_height)

# Initialize the last known position
last_x, last_y = 0, 0

while keyboard.is_pressed("q") == False:
    # Capture the specified screen area
    img = ImageGrab.grab(capture_area)
    img_np = np.array(img)
    
    # Convert the captured image to RGB and then to HSV
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the HSV range for detecting the target color (bright white)
    h_min = np.array((0, 0, 253), np.uint8)
    h_max = np.array((255, 0, 255), np.uint8)
    
    # Create a mask based on the HSV range
    mask = cv2.inRange(frame_hsv, h_min, h_max)
    
    # Calculate moments of the mask
    moments = cv2.moments(mask, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    
    if dArea > 0:
        current_x = int(dM10 / dArea)
        current_y = int(dM01 / dArea)
        
        # Check if there is significant movement
        if last_x > 0 and last_y > 0:
            if abs(current_x - last_x) > 5 or abs(current_y - last_y) > 5:
                print("Movement detected")
        
        # Update the last known position
        last_x, last_y = current_x, current_y
    
    # Add a small delay to prevent excessive CPU usage
    time.sleep(0.1)