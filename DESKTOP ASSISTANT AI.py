import speech_recognition as sr 
import pyttsx3
import datetime
import time
import webbrowser
import pywhatkit
import pyjokes

AI = pyttsx3.init()
def speak(text):
    AI.say(text)
    AI.runAndWait()
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am Listening Lumi,please say something")
        recognizer.pause_threshold = 0.8
        audio = recognizer.listen(source)
    try:
        print("Recognizing....")
        query = recognizer.recognize_google(audio,language="en-in")
        return query
    except Exception as e:
        print("Sorry Lumi, I could not understand..")
        speak("Sorry Lumi, I could not understand")
        return None

        
def telltime():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")  # 12-hour format with AM/PM
    print(f"The current time is {current_time}")
    time.sleep(0.2)
    speak(f"The current time is {current_time}")

def openweb(sitename):
    
    sites = {"youtube": "https://www.youtube.com/",
    "google":"https://www.google.com/",
    "gmail" : "https://mail.google.com/mail/u/0/#inbox",
    "pythoncompiler" : "https://www.onlinegdb.com/", }
    url = sites.get(sitename.lower())
    if url:
        speak(f"Opening {sitename}")
        chrome_path ="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url)
        webbrowser.open(url)
    else:
        speak(f"Sorry,I dont know {sitename}")
        
def playyoutube(song):
    speak(f"Playing {song} on Youtube")
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(f"https://www.youtube.com/results?search_query={song}")
def telljoke():
    joke = pyjokes.get_joke(language="en", category="neutral")
    speak(joke)

if __name__ == "__main__":
    speak("Hello Lumi,I am your Desktop Assistant.How can I help you")
    while True:
        command = take_command()
        if command:
           command = command.lower()
           print(f"recognized: {command}")
           if "time" in command:
               telltime()
           elif "open" in command:
               site = command.replace("open","").strip().lower()
               openweb(site)
           elif "play" in command:
               song = command.replace("play","").strip()
               playyoutube(song)
           elif "joke" in command:
               telljoke()
           elif "exit" in command or "stop" in command:
               speak("Goodbye lumi.")
               break
           else:
              speak("Sorry,I don't know that command yet.")

