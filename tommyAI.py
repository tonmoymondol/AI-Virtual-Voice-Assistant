import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring!")
    elif hour>=12 and hour<18:
        speak("Good Afternood")
    else:
        speak("Good Evening!")

    speak("Hi! I am your virtual assistant sir. Please tell me how can I help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!")
        audio = r.listen(source, timeout=1, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-us')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tonmoytonoy04@gmail.com','L0vey0uMA')
    server.sendmail('tonmoymondol04@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    #while True:
    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'G:\\SongS'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'email to buddy' in query:
            try:
                speak("What should I send")
                content = takecommand()
                to = "tonmoymondol04@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir, I was not able to send email due to some technical error")
        elif 'Quit' in query:
            exit()