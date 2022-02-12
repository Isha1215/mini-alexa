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
import requests
from bs4 import BeautifulSoup
import os
import PyPDF2 #pdf reader
import speedtest
import cv2
import operator
import pyautogui #volume control
import smtplib
import alarm #self package
import psutil #battery percentage

engine=pyttsx3.init('sapi5')  #sapi5 -api (speech synthesis)(text-speech)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',130)
##########################
def calculate(query,math_dict):
    l=query.split(" ")
    n1=int(l[0])
    n2=int(l[-1])
    temp=l[1:-1]
    print(temp)
    s=" "
    s=s.join(temp)
    oper=math_dict[s]
    ans=oper(n1,n2)
    return ans
##########################
def send_mail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)  #Simple mail transfer protocol
    server.ehlo()  #initiaties the smtp client session
    server.starttls() #starts a tls handshake for secure session
    server.login('pizza27015@gmail.com','park@jimin078')
    server.sendmail('pizza27015@gmail.com',to,content)
    server.close()

##########################
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

##########################
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print("Start speaking....")
        print('Listening.....')
        engine_talk("Listening")
        audio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(audio,language='en-us')
        command=command.lower()
    except Exception as ex:
        return None
    return command

##########################
phone_dict={'swati':'+919665812591','father':'+919822557291'}
email_dict={'bts':'pizza27015@gmail.com','joey':'joey@gmail.com'}
math_dict={'+':operator.add,'-':operator.sub,'x':operator.mul,'/':operator.truediv,'modulus':operator.mod,'raised to':operator.pow,'raise to':operator.pow,'to the power':operator.pow}


def run_alexa():
    try:
        command=take_command()
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
        elif 'temperature' in command:
            city='pune'
            url='https://www.google.com/search?q=weather'+city
            info=requests.get(url)
            html=BeautifulSoup(info.text,'html.parser')
            temp=html.find('div',attrs={'class':'BNeawe'}).text
            print('Temperature right now is ',temp)
            engine_talk(f"Temperature right now is {temp}")
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
        elif 'read pdf' in command:
            try:
                book=open('file.pdf','rb')
                pdf_reader=PyPDF2.PdfFileReader(book)
                num_pages=pdf_reader.numPages
                print('The number of pages in the pdf are ',num_pages)
                engine_talk(f'The number of pages in the pdf are {num_pages}')
                print('Which page you would want me to read?')
                engine_talk('Which page you would want me to read?')
                num=take_command()
                num=int(num)
                page=pdf_reader.getPage(num)
                text=page.extractText()
                print(text)
                engine_talk(text)
            except Exception as e:
                print('Error occurred')
                engine_talk('Error occurred')
        elif 'math' in command or 'calculations' in command:
            try:
                print('What calculations do you wish to perform? For example 2+2')
                engine_talk('What calculations do you wish to perform? For example 2+2')
                query=take_command()
                print(query)
                ans=calculate(query,math_dict)
                print(query+'is equal to ',ans)
                engine_talk(f'{query} is equal to {ans}')
            except Exception as e:
                print('There was some error with the command')
                engine_talk('There was some error with the command')
        elif 'open command prompt' in command:
            print('Opening command prompt...')
            engine_talk('Opening command prompt')
            os.system('start cmd')
        elif 'open webcam' in command:
            print('Opening web cam...')
            engine_talk('Opening web cam')
            cap = cv2.VideoCapture(0)
            while True:
                success,img=cap.read()
                cv2.imshow('img',img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif 'battery' in command or 'battery percentage' in command:
                battery=psutil.sensors_battery()  #battery info
                percentage=battery.percent
                print(f'your system battery is {percentage} percent')
                engine_talk(f'your system battery is {percentage} percent')
        elif 'internet speed' in command:
            st=speedtest.Speedtest()
            ds=int(st.download())
            us=int(st.upload())
            print(f'You have {ds} per second downloading speed and {us} per second uploading speed')
            engine_talk(f'You have {ds} per second downloading speed and {us} per second uploading speed')
        elif 'change window' in command:
            import time
            print('Changing window')
            engine_talk('Changing window')
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        elif 'close notepad' in command:
            print('Closing notepad')
            engine_talk('Closing Notepad')
            os.system('taskkill /f /im notepad.exe')
        elif 'set alarm' in command:
            try:
                print('Tell me the time to set the alarm please , for example set alarm at 2:30 AM')
                engine_talk('Tell me the time to set the alarm please , for example set alarm at 2:30 AM')
                timing=take_command()
                timing=timing.replace('set alarm at ','')
                timing=timing.replace('.','')
                timing=timing.upper()
                print("Setting alarm at",timing)
                engine_talk("Setting alarm at"+timing)
                alarm.set_alarm(timing)
            except Exception as e:
                print("Sorry error occurred",e)
                engine_talk("Sorry error occurred")

        elif 'message' in command:
            try:
                print('To whom you wish to send a message')
                engine_talk('To whom you wish to send a message')
                name=take_command()
                phone_no=phone_dict[name]
                engine_talk("Okay and what should i send??")
                print("Okay and what should i send??")
                msg=take_command()
                h=datetime.datetime.now().hour
                m=datetime.datetime.now().minute
                pywhatkit.sendwhatmsg(phone_no,msg,h,m+2)
            except Exception as e:
                print('Sorry!! i could not place the message due to some error')
        elif 'send email' in command:
            try:
                print('To whom should i send??')
                engine_talk('To whom should i send?')
                name = take_command()
                email=email_dict[name]
                print(' Okay and what should i say?')
                engine_talk('Okay and what should i say?')
                content=take_command()
                print('Sending email')
                engine_talk('Sending email')
                send_mail(email,content)
                print('Sent email successfully')
                engine_talk('Sent email successfully')
            except Exception as e:
                print('Sorry error occured')
                engine_talk('Sorry error occured')
                print(e)
        elif 'volume up' in command:
            print('Increasing Volume')
            engine_talk('Increasing volume')
            pyautogui.press("volumeup")
        elif 'volume down' in command:
            print('Decreasing Volume')
            engine_talk('Decreasing volume')
            pyautogui.press("volumedowm")
        elif 'volume mute' in command:
            print('Muting Volume')
            engine_talk('Muting volume')
            pyautogui.press("volumemute")
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
        elif 'shutdown' in command:
            print('Shutting down..')
            engine_talk('Shutting down')
            os.system('shutdown /s /t 5')
        elif 'restart' in command:
            print('Restarting the system')
            engine_talk('Restarting the system')
            os.system('taskkill /r /t 5')
        elif 'sleep the system' in command:
            print('Putting the system to sleep')
            engine_talk('Putting the system to sleep')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        else:
            search='https://www.google.com/search?q='+command
            print('Here is what i found on the internet')
            engine_talk('Here is what i found on the internet')
            wb.get().open(search)
    except Exception as e:
        print('Say that again')
        engine_talk('Say that again')




print('Clearing background noises....Please wait...')
engine_talk('Clearing background noises....Please wait...')
print('Hello i am alexa how may i help you')
engine_talk('Hello i am alexa how may i help you')

while True:
    run_alexa()






