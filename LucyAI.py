import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour) 
    if hour>=4 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else: 
        speak("Good Evening!")
    speak("I am Lucy Sir, Please tell me how may i help you?")  

def takeCommand():
    #It takes mcrophone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio,language='en-in')   
        print(f"User said: {query}\n")

    except Exception :
        #print(e)
        print("Say that again please sir...")
        speak("Say that again please sir...")
        return "None"
    return query  

def sendEmail(to,content):
    with open("mypass.txt", 'r') as f:
        MyPassCode = (f.read())
    mystr=''
    MyP=mystr.join(MyPassCode)  
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rexina0007@gmail.com',MyP)
    server.sendmail('rexina0007@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 
        
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")   

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")     

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open github' in query:
            webbrowser.open("github.com")   

        elif 'play music' in query:
            music_dir = 'D:\\MyMusic' #enter your path
            songs = os.listdir(music_dir) 
            n = random.randint(0,4)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[n]))     
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\SUBHAMREX\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #enter your path
            os.startfile(codepath)
        
        elif 'send mail' in query:
            try:
                speak("What should I say?")  
                content = takeCommand()
                to = "subhamkundu486@gmail.com" 
                sendEmail(to,content) 
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am unable to send this mail at the momment")

        elif 'what\'s your name?' in query:
            speak("my name is lucy") 
            print("my name is lucy")       
                
        elif 'bye bye' in query:
            speak("bye sir, talk you later")
            sys.exit()    
                   

