import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 1.0)
    engine.say(" ")
    engine.say(message)
    engine.runAndWait()