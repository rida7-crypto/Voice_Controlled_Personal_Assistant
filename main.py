from listener import listen
from speech import speak
from command_handler import handle_command

def main():
    while True:
        command = listen()
        if "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye Rida! Hope to see you soon!")
            break
        elif "hello" in command:
            speak("Hello Rida. How may I help you?")
        else:
            handle_command(command)

if __name__ == "__main__":
    main()