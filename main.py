#Libraries used
#speech_recognition (speech<->text)
#PyAudio (Pre-requisite for speech_recognition) (Microphone users)
#pywhatkit (automation tasks) (send message/email/play yt etc)
#pyttsx3 (convert text into voice)
#pyjokes (create jokes)
import pyttsx3
import webbrowser as wb
import speech_recognition as sr
import pywhatkit
import pyjokes
from datetime import date
import datetime
import wikipedia
import sys
import os
import cv2
cap=cv2.VideoCapture(0)
engine=pyttsx3.init('sapi5')  #sapi5 -api (speech synthesis)(text-speech)
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',130)
recognizer=sr.Recognizer()
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
#engine_talk("hello how are you")

def run_alexa():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print('\n')
        print("Start speaking....")
        print('Listening.....')
        engine_talk("Listening")
        audio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(audio,language='en-us')
        command=command.lower()
        if 'alexa' in command:
            command=command.replace('alexa','')
            print('you said',command)
        else:
            print('you said',command)
        if 'hello' in command:
            print('Hello how can i help you?')
            engine_talk('Hello how can i help you?')
        elif 'who are you' in command:
            print('I am Alexa aka your virtual assistant')
            engine_talk('I am Alexa aka your virtual assistant')
        elif 'can you do' in command:
            print('''
            I can play songs on youtube,tell a joke, tell date and time, search on wikepedia, find your location,
            locate any area on maps, open websites like youtube,instagram,git hub,stack overflow and searches on google.
            How may i help you?
            ''')
            engine_talk('''I can play songs on youtube,tell a joke, tell date and time, search on wikepedia, find your location,
            locate any area on maps, open websites like youtube,instagram,git hub,stack overflow and searches on google.
            How may i help you?
            ''')
        elif 'play' in command:
            song=command.replace('play','')
            print('Playing',song)
            engine_talk('Playing'+song)
            pywhatkit.playonyt(song)
        elif 'date and time' in command:
            today=date.today()
            time=datetime.datetime.now().strftime('%I:%M %p')
            today=today.strftime('%B %d %Y')
            print("Today's date is", today,"and current time is",time)
            engine_talk("Today's date is"+today)
            engine_talk("and current time is"+time)
        elif 'time and date' in command:
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            today = today.strftime('%B %d %Y')
            print("Current time is", time, "and Today's date is", today)
            engine_talk("Current time is" + time)
            engine_talk(" and Today's date is" + today)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print("Current time is", time)
            engine_talk("Current time is" + time)
        elif 'date' in command:
            today=date.today()
            today = today.strftime('%B %d %Y')
            print("Today's date is" + today)
            engine_talk("Today's date is" + today)
        elif 'tell me about' in command:
            command=command.replace('tell me about','')
            info=wikipedia.summary(command,1)
            print(info)
            engine_talk(info)
        elif 'what is' in command:
            command = command.replace('what', '')
            info = wikipedia.summary(command, 1)
            print(info)
            engine_talk(info)
        elif 'who is' in command:
            command = command.replace('who is', '')
            info = wikipedia.summary(command, 1)
            print(info)
            engine_talk(info)
        elif 'what is' in command:
            search='https://www.google.com/search?q='+command
            wb.open(search)
            print('This is what is found on the internet..')
            engine_talk('This is what is found on the internet..')
        elif 'search' in command:
            search='https://www.google.com/search?q='+command
            print('Searching...')
            engine_talk('Searching...')
            wb.open(search)
        elif 'my location' in command:
            loc="https://www.google.com/maps/search/Where+am+I+?/"
            print("Your location is somewhere near here..")
            engine_talk('Your location is somewhere near here..')
            wb.get().open(loc)
        elif 'joke' in command:
            joke=pyjokes.get_joke()
            print(joke)
            engine_talk(joke)
        elif 'locate' in command:
            print('locating...')
            command=command.replace('locate','')
            if 'on map' in command:
                command=command.replace('on map','')
            loc= 'https://google.nl/maps/place/'+command +'/&amp;'
            print('Here is the location of ',command)
            engine_talk('Here is the location of '+command)
            wb.get().open(loc)
        elif 'on map' in command:
            print('locating...')
            com=command.split(" ")
            loc='https://google.nl/maps/place/'+com[1]+'/&amp;'
            print('Here is the location of ',com[1])
            engine_talk('Here is the location of '+com[1])
            wb.get().open(loc)
        elif 'location of' in command:
            print('locating...')
            command=command.replace('find location of','')
            loc = 'https://google.nl/maps/place/' + command + '/&amp;'
            print('Here is the location of ', command)
            engine_talk('Here is the location of ' + command)
            wb.get().open(loc)
        elif 'where is' in command:
            print('locating...')
            command=command.replace('where is' ,'')
            loc = 'https://google.nl/maps/place/' + command + '/&amp;'
            print('Here is the location of ', command)
            engine_talk('Here is the location of ' + command)
            wb.get().open(loc)
        elif 'open youtube' in command:
            url='https://www.youtube.com/'
            print('Opening youtube..')
            engine_talk('Opening youtube..')
            wb.open_new(url)
        elif 'open google' in command:
            url = 'https://www.google.com/'
            print('Opening google..')
            engine_talk('Opening google..')
            wb.open_new(url)
        elif 'open gmail' in command:
            url = 'https://mail.google.com/mail/u/0/#inbox'
            print('Opening gmail..')
            engine_talk('Opening gmail..')
            wb.open_new(url)
        elif 'open instagram' in command:
            url = 'https://www.instagram.com/'
            print('Opening instagram..')
            engine_talk('Opening instagram..')
            wb.open_new(url)
        elif 'open stack overflow' in command:
            url = 'https://stackoverflow.com/'
            print('Opening stack overflow..')
            engine_talk('Opening stack overflow..')
            wb.open_new(url)
        elif 'open git hub' in command:
            url = 'https://github.com/'
            print('Opening git hub..')
            engine_talk('Opening git hub')
            wb.open_new(url)
        elif 'open notepad' in command:
            print('Opening notepad')
            engine_talk('Opening notepad')
            loc='C:\\Windows\\System32\\notepad.exe'
            os.startfile(loc)
        elif 'open command prompt' in command:
            print('Opening command prompt...')
            engine_talk('Opening command prompt')
            os.system('start cmd')
        elif 'open web cam' in command:
            print('Opening web cam...')
            engine_talk('Opening web cam')
            while True:
                success,img=cap.read()
                cv2.imshow('img',img)
        elif 'close web cam' in command:
            print('Closing web cam')
            engine_talk('Closing web cam')
            cap.release()
            cap.destroyAllWindows()
        elif 'bye' in command:
            print('Bye, have a nice day!!')
            engine_talk('Bye, have a nice day!!')
            sys.exit()
        elif 'stop' in command:
            print('Bye, have a nice day!!')
            engine_talk('Bye, have a nice day!!')
            sys.exit()
        elif 'end' in command:
            print('Bye, have a nice day!!')
            engine_talk('Bye, have a nice day!!')
            sys.exit()
        else:
            search='https://www.google.com/search?q='+command
            print('Here is what i found on the internet')
            engine_talk('Here is what i found on the internet')
            wb.get().open(search)
    except Exception as ex:
        print(ex)

print('Clearing background noises....Please wait...')
engine_talk('Clearing background noises....Please wait...')
print('Hello i am alexa how may i help you')
engine_talk('Hello i am alexa how may i help you')

while True:
    run_alexa()







