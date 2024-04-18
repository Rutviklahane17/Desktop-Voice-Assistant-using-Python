import pyttsx3;
import datetime
import speechRecognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)




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
        speak('Good Evening!')

    speak("may Alvin hu . aapki kya madut kar saktaa hu")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,Language = 'en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        # print(e)

        print('say it again please.....')
        return "None"
    return query





if __name__=="__main__":
    wishMe()
    takeCommand()