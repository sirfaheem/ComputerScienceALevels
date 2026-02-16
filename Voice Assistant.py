import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to take the user's speech input
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            command = take_command()
        
        return command.lower()

# Define functions for different tasks
def set_reminder():
    print("Sure, I'll help you set a reminder.")

def create_todo():
    print("Alright, let's create a to-do list.")

def search_web():
    print("What would you like me to search for?")

# Start the assistant
while True:
    command = take_command()

    if "set a reminder" in command:
        set_reminder()
    elif "create a to-do list" in command:
        create_todo()
    elif "search the web" in command:
        search_web()
    elif "exit" in command:
        break
    else:
        print("Sorry, I didn't understand that command. Please try again.")
