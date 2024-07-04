import pyautogui
import cv2
import numpy as np
import time
import keyboard

def main():
    count = 0
    print("Red motion detection started. Press 'q' to stop.")
    while count <= 15 and not keyboard.is_pressed('q'):
        result = detect_red_motion()
        if result:
            x, y = result
            print(f"Red motion detected at: {x}, {y}")
            count += 1
        time.sleep(0.1)  # Add a small delay to reduce CPU usage

def detect_red_motion():
    # Capture the initial screen
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    
    # Get the screen dimensions
    height, width = screen.shape[:2]
    
    # Define the region of interest (lower half of the screen)
    roi = screen[height//2:, :]
    
    # Convert to HSV color space
    prev_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    prev_centroid = None
    cooldown = 0
    
    while not keyboard.is_pressed('q'):
        try:
            # Capture the current screen
            current_screen = pyautogui.screenshot()
            current_screen = cv2.cvtColor(np.array(current_screen), cv2.COLOR_RGB2BGR)
            
            # Get the lower half
            current_roi = current_screen[height//2:, :]
            
            # Convert to HSV color space
            current_hsv = cv2.cvtColor(current_roi, cv2.COLOR_BGR2HSV)
            
            # Define range for red color and create a mask
            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(current_hsv, lower_red, upper_red)
            
            lower_red = np.array([170, 120, 70])
            upper_red = np.array([180, 255, 255])
            mask2 = cv2.inRange(current_hsv, lower_red, upper_red)
            
            mask = mask1 + mask2

            # Calculate the total number of red pixels
            red_pixel_count = np.sum(mask > 0)
            
            # Only proceed if there's a significant amount of red
            if red_pixel_count > 1000:  # Adjust this threshold as needed
                # Calculate centroid of the red area
                centroid = calculate_centroid(mask)
                
                # Calculate the difference between the current and previous frame
                diff = cv2.absdiff(prev_hsv, current_hsv)
                
                # Apply the red mask to the difference
                red_diff = cv2.bitwise_and(diff, diff, mask=mask)
                
                # If there's significant difference in the red areas, motion is detected
                if np.sum(red_diff) > 10000 and cooldown == 0:  # Increased threshold
                    if centroid and (prev_centroid is None or np.linalg.norm(np.array(centroid) - np.array(prev_centroid)) > 10):
                        prev_centroid = centroid
                        cooldown = 20
                        print(f"Red pixel count: {red_pixel_count}")
                        print(f"Motion difference sum: {np.sum(red_diff)}")
                        return (centroid[0], height//2 + centroid[1])  # Adjust y-coordinate

            
            # Update the previous frame
            prev_hsv = current_hsv
            
            # Decrease cooldown
            if cooldown > 0:
                cooldown -= 1
            
            # Small delay to reduce CPU usage
            time.sleep(0.1)
            
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    return None

def calculate_centroid(mask):
    # Calculate moments of the mask
    M = cv2.moments(mask)
    
    # Calculate centroid
    if M["m00"] > 1000:  # Increased minimum area threshold
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return (cX, cY)
    return None

if __name__ == "__main__":
    main()