import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import psutil
import os
import pyautogui
import wikipedia
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
    except:
        speak("I didn't get that")
        return "none"
    return query


name = input("Enter your name : ")


def wishme():
    hour = datetime.datetime.now().hour
    if 0 < hour < 12:
        print(f"Good morning, {name}")
        speak(f"Good morning, {name}")
    elif 12 <= hour < 16:
        print(f"Good afternoon, {name}")
        speak(f"Good afternoon, {name}")
    else:
        print(f"Good evening, {name}")
        speak(f"Good evening, {name}")


wishme()

print("I am your Virtual Voice Assistant, please tell how may I help you")
speak("I am your Virtual Voice Assistant, please tell how may I help you")

while True:

    query = takecommand().lower()

    if "hello" in query:
        print("Hello dear")
        speak("Hello dear")

    elif "how are you" in query:
        speak("I am fine, thank you. How are you?")
        user_reply = takecommand().lower()

        if 'well' in user_reply or 'fine' in user_reply or 'good' in user_reply:
            speak("That's good to hear!")
        elif "not good" in user_reply or "sad" in user_reply or "tired" in user_reply:
            speak("Oh, take some rest. You’ll feel better soon.")
        else:
            speak("I see. Take care of yourself.")

    elif 'exit' in query:
        print("Ok I am going offline")
        speak("OK I am going offline")
        exit()

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'open whatsapp' in query:
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open facebook' in query:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif 'open instagram' in query:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif 'battery' in query:
        battery = psutil.sensors_battery().percent
        speak(f"Battery is {battery} percent")
        print(f"Battery is: {battery}%")

    elif 'open notepad' in query:
        speak("Opening notepad")
        os.system("notepad.exe")

    elif 'write it down' in query:
        speak("Tell me what to write")
        text = takecommand()
        pyautogui.typewrite(text, 0.1)

    elif 'volume up' in query:
        speak("Volume up")
        pyautogui.press("volumeup")

    elif 'volume down' in query:
        speak("Volume down")
        pyautogui.press("volumedown")

    elif 'volume mute' in query:
        speak("Volume muted")
        pyautogui.press("volumemute")

    elif 'volume unmute' in query:
        speak("Volume unmuted")
        pyautogui.press("volumeup")

    elif 'wikipedia' in query:
        speak("Searching Wikipedia")
        search = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(search, sentences=3)
        print(results)
        speak(results)

    elif 'time' in query:
        current_time = time.strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
        print(f"The time is {current_time}")
