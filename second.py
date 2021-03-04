import pyttsx3
import datetime
import pywin32_bootstrap
import win32api
#import pyaudio
from PIL import Image
import urllib3
import os
import wikipedia
import speech_recognition as sr
import webbrowser
# imppy('voice',voices[0].id)
engine = pyttsx3.init()
# voices=engine.getProperty('voices')
# print(voices.id)
engine.setProperty('rate',150)
# engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour>=12 and hour<17:
        speak('good afternoon sir')
    else:
        speak('good evening sir')
    speak("I am friday . your personal assistant")
    speak("how may I help you")
def takeCommand ():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("recognising..")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again")
        return "none"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')
        elif 'play music' in query:
            music_dir='C:\\Users\\Public\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'open image' in query:
            img1=Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures')
            img1.show()

        elif 'close' in query:
            speak("bye sir")
            exit()


