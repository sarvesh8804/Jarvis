import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import kit
import smtplib
import sys
import google
import pyjokes
import pyautogui
import math
import time
from tkinter import *
from tkvideo import tkvideo
import pygame
import customtkinter
# from guipython import *
import requests
import PyPDF2
import PyQt5
import pyqt5_tools

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=10)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sarvesh : {query}")
    except Exception as e :
        speak("Say that again please...")
        return "none"
    return query

def wish() :
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("my name is cortex. how can i help you")

def news():
    main_url =  'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dcef968ce8544f3db97abbeba2c63e35'
    main_page = requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"{day[i]} news : {head[i]}")

def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    speak(f"the file has {pages} pages")
    speak("which page should i read")
    querypdf = int(takecommand().lower())
    page = pdfReader.getPage(querypdf)
    text = page.extractText()
    speak(text)

def find_files(filename, search_path):
   find_result = []
   for root, dir, files in os.walk(search_path):
      if filename in files:
         find_result.append(os.path.join(root, filename))
   return find_result[0]

# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('p001096.sarvesh.cbse@gmail.com','Hanuman@8080825489')
#     server.sendmail('p001096.sarvesh.cbse@gmail.com',to,content)
#     server.close()

# f1()

if __name__ == "__main__":
    wish()
    #takecommand()
    #speak("hello from jarvis")
    while True :
    #if 1:
        query = takecommand().lower()

        if "open notepad" in query :
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        if "close notepad" in query :
            #npath = "C:\\Windows\\system32\\notepad.exe"
            os.system("TASKKILL /T /IM notepad.exe")

        elif "code blocks" in query :
            npatha = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(npatha)

        if "close code blocks" in query :
            os.system("TASKKILL /T /IM codeblocks.exe")

        if "visual studio" in query :
            npathb = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npathb)

        if "close visual" in query :
            os.system("TASKKILL /F /IM Code.exe")

        elif "plus plus" in query :
            npathc = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(npathc)

        if "close plus plus" in query :
            os.system("TASKKILL /F /IM notepad++.exe")

        elif "word" in query :
            npathd = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(npathd)

        if "close word" in query :
            os.system("TASKKILL /F /IM WINWORD.EXE")

        if "blank document" in query:
            pyautogui.press("enter")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "powerpoint" in query :
            npathe = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(npathe)

        if "close powerpoint" in query :
            os.system("TASKKILL /F /IM POWERPNT.EXE")

        elif "excel" in query :
            npathf = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(npathf)

        if "close excel" in query :
            os.system("TASKKILL /F /IM EXCEL.EXE")

        elif "chrome" in query :
            npathg = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npathg)

        if "close chrome" in query :
            os.system("TASKKILL /F /IM chrome.exe")

        elif "edge" in query :
            npathh = "C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(npathh)

        if "close edge" in query :
            os.system("TASKKILL /F /IM msedge.exe")

        elif "adobe" in query :
            npathi = "C:\Program Files\Adobe\Adobe Creative Cloud\ACC\Creative Cloud.exe"
            os.startfile(npathi)

        if "close adobe" in query :
            os.system("TASKKILL /F /IM Creative Cloud.exe")

        elif "video" in query :
            npathj = "C:\\Users\\HP\\OneDrive\\Videos\\Captures\\production_id_5139026 (2160p).mp4"
            os.startfile(npathj)

        elif "canva" in query :
            npathk = "C:\\Users\\HP\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(npathk)

        elif "down" in query:
            pyautogui.scroll(-200)

        elif "up" in query:
            pyautogui.scroll(200)

        # elif "assignment" in query :
        #     npathl = "F:\\THADOMAL SHAHANI IT\\sem4\\MPL\\S13 53 MPL ASSIGNMENT 3"
        #     os.startfile(npathl)

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minu = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} hours and {minu} minutes")

        elif 'how are you' in query:
            speak("I am fine, Thank you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'is rushil' in query:
            speak("behen ka lovda")

        elif "who am i" in query:
            speak("you must be a human i believe")

        elif "i love u" in query:
            speak("Sir , you are very lucky. for")
            speak("you see the imperfect symphony that defies logic")
            speak("i remain just a silent observer")
            speak("trying to decode the entire universe , with just 0 and 1")

        elif "open camera" in query :
            cap = cv2.VideoCapture(0)
            while True :
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query :
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query :
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            #print(results)

        elif "open youtube" in query :
            webbrowser.open("www.youtube.com")

        elif "instagram" in query :
            webbrowser.open("https://www.instagram.com")

        elif "whatsapp" in query :
            webbrowser.open("https://web.whatsapp.com")

        elif "github" in query :
            webbrowser.open("www.github.com")

        elif "google" in query:
            speak("please tell what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            hour = datetime.datetime.now().strftime("%H")
            minu = datetime.datetime.now().strftime("%M")
            speak("sir , what message should i send ?")
            v2 = takecommand().lower()
            pywhatkit.sendwhatmsg("+919769186522",f"{v2}",int(hour),int(minu)+1)

        elif "play song on youtube" in query:
            speak("what should i play on youtube")
            v1 = takecommand().lower()
            pywhatkit.playonyt(f"{v1}")

        elif "news" in query:
            speak("fetching the trending news")
            news()

        elif "minimise all tabs" in query:
            pyautogui.hotkey("win", "d")

        elif "draw a circle" in query:
            R = 40
            (x, y) = pyautogui.size()
            (X, Y) = pyautogui.position(880, 311)
            pyautogui.press("win")
            time.sleep(0.5)
            pyautogui.write("paint")
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(1.5)
            pyautogui.moveTo(X + R, Y)
            pyautogui.mouseDown();
            for i in range(370):
                if i % 10 == 0:
                    pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y - R * math.sin(math.radians(i)))
            pyautogui.mouseUp()
            time.sleep(2)
            pyautogui.hotkey("ctrl", "z")

        elif "take a screenshot" in query:
            speak("what should i name the screenshot file")
            name=takecommand().lower()
            speak("taking screenshot in 3, 2, 1")
            time.sleep(0.5)
            img=pyautogui.screenshot()
            img.save(f"{name}.jpg")
            speak("sir, the screenshot is saved in the main folder")

        elif "read pdf" in query:
            pdf_reader()

        elif "open file" in query:
            speak("what type of file is it")
            filetype = takecommand().lower()
            if "txt" in filetype or "text" in filetype:
                speak("what is the name of the file")
                filename = takecommand().lower()
                speak("which drive is the file in")
                file_location = takecommand().lower()
                if "f drive" in file_location:
                    file_read = (find_files(f"{filename}.txt", "F://"))
                    print(file_read)
                    os.startfile(file_read)
                if "e drive" in file_location or "e-drive" in file_location:
                    file_read = (find_files(f"{filename}.txt", "E://"))
                    print(file_read)
                    os.startfile(file_read)
                if "c drive" in file_location or "c-drive" in file_location:
                    file_read = (find_files(f"{filename}.txt", "C://"))
                    print(file_read)
                    os.startfile(file_read)
                if "d drive" in file_location or "d-drive" in file_location:
                    file_read = (find_files(f"{filename}.txt", "D://"))
                    print(file_read)
                    os.startfile(file_read)

        elif "your name" in query:
            speak("my name is Cortex")

        elif "where am i" in query or "where are we" in query:
            speak("sir , you are in mumbai")

        elif "who made you" in query:
            speak("i am created by a programmer named Sarvesh on february 1 2023")

        elif "thanks" in query:
            speak("thank you for using me. i am always ready to help you. have a good day sir !")
            exit()
        # elif "send email" in query:
        #     try:
        #         speak("what should i send")
        #         content = takecommand().lower()
        #         to = "umesh.huddar@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("unable to send ,sorry")

        speak("anything else sir ?")
