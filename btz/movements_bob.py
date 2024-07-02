import cv2
import numpy as np
import pyautogui
import keyboard

def detect_red_icon_movement(threshold=70):
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Calculate the bounds for the center third of the screen
    left = 0
    top = screen_height // 2
    width = screen_width
    height = screen_height // 2

    # Take two screenshots of the specified area in quick succession
    screenshot1 = pyautogui.screenshot(region=(left, top, width, height))
    screenshot2 = pyautogui.screenshot(region=(left, top, width, height))

    # Convert the screenshots to numpy arrays
    frame1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)
    frame2 = cv2.cvtColor(np.array(screenshot2), cv2.COLOR_RGB2BGR)

    # Convert to HSV color space
    hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    # Define range for red color
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Create masks for red color
    mask1 = cv2.inRange(hsv1, lower_red, upper_red)
    mask2 = cv2.inRange(hsv2, lower_red, upper_red)

    # Calculate the difference between the two masks
    diff = cv2.absdiff(mask1, mask2)

    # Count non-zero pixels in the difference image
    movement = np.count_nonzero(diff)

    return movement > threshold

# Example usage
if __name__ == "__main__":
    print("Detecting red icon movement on the primary monitor...")
    print("Press Ctrl+C to stop the script.")
    
    try:
        while keyboard.is_pressed("q") == False:
            if detect_red_icon_movement():
                print("Red icon movement detected!")
            else:
                print("No movement detected.")
            pyautogui.sleep(0.3)  # Add a small delay to prevent excessive CPU usage
    except KeyboardInterrupt:
        print("\nScript stopped by user.")