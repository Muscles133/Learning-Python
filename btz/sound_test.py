import pyautogui, time, keyboard, os
import numpy as np
import soundcard as sc

def reel_in():
    # seconds_timer = 0
    # global reeled

    while True:
        reeled = False

        # If the escape key is pressed, exit the program
        if keyboard.is_pressed('esc') == True:
            print("<< Exiting >>")
            exit()
        # If the user selected the default speakers as the audio output device
        if input_device == '1':
            audio_source = sc.default_speaker().name
        # If the user selected VoiceMeeter as the audio output device
        if input_device == '2':
            audio_source = sc.get_speaker('VoiceMeeter Input').name
        # Get the microphone that corresponds to the selected audio output device
        mic = sc.get_microphone(id=audio_source, include_loopback=True)
        # Record audio from the microphone
        data = mic.record(samplerate=48000, numframes=48000)
        # Calculate the peak of the audio signal
        audio_peak = np.max(abs(data))
        seconds_timer += 1

        # If the audio peak is greater than 0.06
        if audio_peak > 0.06:
            print("<< You (hopefully) caught something! >>\n")
            # Simulate a right mouse button click
            # pyautogui.mouseDown(button='right')
            # time.sleep(np.random.uniform(0.03,0.08))
            # pyautogui.mouseUp(button='right')
            # time.sleep(np.random.uniform(0.35,0.5))
            # reeled = True
            break

        # If the timer has exceeded 12 seconds
        # if seconds_timer > 12:
        #     print("<< Failed. Trying again. >>")
        #     break

reel_in()

