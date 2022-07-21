#Dependencies-

#pip install matplotlib
#pip install numpy
#pip install pyttsx3
#pip install speechRecognition
#pip install Pyaudio
#pip install pypiwin32
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
    # if 1:
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
            webbrowser.open("https://github.com/")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The current time is {strTime}")

        elif 'wikipedia' in query:
            webbrowser.open("https://en.wikipedia.org/wiki/Ultron")
        elif 'who are you' in query:
            speak("I am Ultron A.I. Please tell how may I help you.")
            print("I am Ultron A.I. Please tell how may I help you.")

            #--------------------------------
#End of the program
