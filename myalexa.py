import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command
    except:
        pass
    return None

def run_alexa():
    command=take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing'+ song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is'+time)
        elif 'who is' in command or 'what is' in command:
            person=command.replace('who is', '')
            info= wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk("sorry, I have a headache")
        elif 'how are you' in command:
            talk("I am chill")
        elif 'are you single' in command:
            talk("I am in a relationship with wifi")
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'stop' in command:
            talk("ok bye")
            sys.exit()
        else:
            talk("Please say the command again")

def run():
    while True:
        run_alexa()

def stop():
    sys.exit()

root = tk.Tk()
root.title("Alexa")
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()
startbutton = tk.Button(text='Start Alexa', command=run, bg='green', fg='green')
canvas1.create_window(150, 150, window=startbutton)
root.mainloop()
