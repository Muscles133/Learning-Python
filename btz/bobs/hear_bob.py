import pyaudio
import numpy as np
import time
import random


def hear_bob():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    THRESHOLD = 1000  # Adjust this value to change sensitivity

    def get_vb_cable_index():
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            dev = p.get_device_info_by_index(i)
            if 'CABLE Output' in dev['name']:
                return i
        return None

    p = pyaudio.PyAudio()

    vb_cable_index = get_vb_cable_index()
    if vb_cable_index is None:
        print("VB-Cable not found. Make sure it's installed and recognized by your system.")
        exit()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=vb_cable_index,
                    frames_per_buffer=CHUNK)

    print("Listening for audio...")

    a = 0
    hearbob = False

    while True:
        try:
            data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
            peak = np.average(np.abs(data)) * 2
            
            if peak > THRESHOLD:
                print("Audio found!")
                hearbob = True
                return hearbob
                break
                
                # time.sleep(1)  # Wait for 1 second before detecting again
        except KeyboardInterrupt:
            print("Stopping...")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    hear_bob()

