import os
import subprocess
from speech import speak
from intents import intent_map, web_intents

def handle_command(command):
    # Check for close intent
    if "close" in command or "exit" in command:
        for app in intent_map:
            if app in command:
                speak(f"Closing {app} for you")
                try:
                    subprocess.call(f"taskkill /f /im {intent_map[app]}", shell=True)
                except Exception as e:
                    speak(f"Couldn't close {app}. Error: {str(e)}")
                return

    # Check for web intents
    for key, data in web_intents.items():
        if any(alias in command for alias in data["aliases"]):
            if "search" in command:
                query = command.split("search", 1)[-1].strip()
                if query:
                    speak(f"Searching {key} for {query}")
                    search_url = data["search_url"].format(query=query.replace(" ", "+"))
                    subprocess.Popen([intent_map["chrome"], search_url])
                    return
            else:
                speak(f"Opening {key} in Chrome")
                subprocess.Popen([intent_map["chrome"], data["url"]])
                return

    # Check for local apps
    for app in intent_map:
        if app in command:
            speak(f"Opening {app} for you")
            os.startfile(intent_map[app])
            return

    speak("Sorry, I don't know that application.")