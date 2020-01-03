import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
'''
python -m pip install speechRecognition --user
python -m pip install pyttsx3 --user
python -m pip install wikipedia --user
python -m pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl --user

'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[0].id)
# print (voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak ("Good Afternoon")
    else:
        speak ("Good Evening")
    speak ("I am Jarvis, your personal assistant. How may I help you?")

def takeCommand():
    '''
    This is for taking input from microphone
    and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,timeout=5,phrase_time_limit=10)

    try:
        print ("Recognizing...")
        query = r.recognize_google(audio , language ='en-in')
        print (f"User said :{query}\n")

    except Exception as e:
        print (e)
        print ("Say that again please ...")
        return "None"
    return query

if __name__ == "__main__":
    # speak("Amit is a good resource")
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open index' in query:
            webbrowser.open("indexprod/")
        elif 'open deployment' in query:
            webbrowser.open("http://automation-deployment-config.msciapps.com/")
        elif 'index monitor' in query:
            webbrowser.open("im.msci.com/")
        elif 'quit jaravi' in query:
            webbrowser.open("im.msci.com/")
