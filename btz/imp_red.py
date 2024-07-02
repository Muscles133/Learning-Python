import cv2
import numpy as np
import pyautogui
import time
import keyboard

def detect_red_movement(threshold=110):
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Define the bottom half of the screen
    left = 0
    top = screen_height // 2
    width = screen_width
    height = screen_height // 2

    # Take two screenshots of the bottom half of the screen in quick succession
    screenshot1 = pyautogui.screenshot(region=(left, top, width, height))
    screenshot2 = pyautogui.screenshot(region=(left, top, width, height))

    # Convert the screenshots to numpy arrays
    frame1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)
    frame2 = cv2.cvtColor(np.array(screenshot2), cv2.COLOR_RGB2BGR)

    # Convert to HSV color space
    hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    # Define range for red color (including both lower and upper red hues)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red color
    mask1_1 = cv2.inRange(hsv1, lower_red1, upper_red1)
    mask1_2 = cv2.inRange(hsv1, lower_red2, upper_red2)
    mask1 = cv2.bitwise_or(mask1_1, mask1_2)

    mask2_1 = cv2.inRange(hsv2, lower_red1, upper_red1)
    mask2_2 = cv2.inRange(hsv2, lower_red2, upper_red2)
    mask2 = cv2.bitwise_or(mask2_1, mask2_2)

    # Calculate the difference between the two masks
    diff = cv2.absdiff(mask1, mask2)

    # Count non-zero pixels in the difference image
    movement = np.count_nonzero(diff)

    return movement > threshold

def main():
    print("Detecting red movement in the bottom half of the screen...")
    print("Press Ctrl+C to stop the script.")

    try:
        while keyboard.is_pressed("q") == False:
            if detect_red_movement():
                print("Movement detected")
            time.sleep(0.3)  # Check every 0.3 seconds
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

if __name__ == "__main__":
    main()