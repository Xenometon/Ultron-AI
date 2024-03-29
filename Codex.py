#Dependencies-

#pip install matplotlib
#pip install numpy
#pip install pyttsx3
#pip install speechRecognition
#pip install Pyaudio
#pip install wikipedia

#Code-

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello there, I am Ultron!. Please tell me how may I help you.")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Could you please say that again...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if (i):
        query = takeCommand().lower()

        # Logic-
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("https://github.com/Xenometon")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The current time is {strTime}")

        elif 'wikipedia' in query:
            webbrowser.open("https://www.wikipedia.org")
        elif 'who are you' in query:
            speak("I am Ultron A.I. Please tell how may I help you.")
            print("I am Ultron. Please vocalize your command...")
        elif 'your name' in query:
            speak("My name is Ultron. I am a AI based Assistant.")
            print("My name is Ultron.")
        elif 'thank you' in query:
            speak("Welcome! Please call me if you need any help.")
            print("This is Ulton, at your assistance...")
        elif 'calculate' in query:
            webbrowser.open("https://www.calculator.net")
            speak("You may use this tool for all your calculation needs.")
            print("Opening Calculator...")

            #--------------------------------
# End of the program
