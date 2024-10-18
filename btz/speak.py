import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What is it?")
cowsay.dragon(this)
engine.say(this)
engine.runAndWait()

