import speech_recognition as sr
import pyttsx3
import os
import click
import pyautogui as pg 

os.startfile(r'C:\dshechka.gif')

start = pyttsx3.init()
r = sr.Recognizer()



    

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("пизди")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration= 1)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:
            task = listen()
        return task




def request(task):
    
    if "привет" in task:
        text = "Наду ками камасай й й й й"
        start.say(text)
        start.runAndWait()
        
    if "поговорим" in task:
        text = "о чём"
        start.say(text)
        start.runAndWait()
        
    if "что ты можешь" in task:
        text = "я могу много вещей, что интересует"
        start.say(text)
        start.runAndWait()
        
    if "пошла н****" in task:
        text = "дохуя умный, мясной мешок"
        start.say(text)
        start.runAndWait()
    
    
    
    if "музыку" in task:
        text = "ВРУБАЮ ЛЮТЫЙ ФОНКККК !!!"
        start.say(text)
        start.runAndWait()
        click.launch("https://vk.com/audios325886448?z=audio_playlist325886448_-21/")
        
        
    if "youtube" in task:
        text = "заебал смотреть свою хуйню"
        start.say(text)
        start.runAndWait()
        click.launch("https://www.youtube.com//")
        
        
    if "открой раст" in task:
        text = "СЮДА, СЮДА, СЮДА"
        start.say(text)
        start.runAndWait()
        pg.hotkey('winleft', 'd')
        pg.click(934, 200)
        pg.click(934, 200)
        
        
    if "открой спайдер" in task:
        text = "смнени раскладку деб б б б, сменил а а а а"
        start.say(text)
        start.runAndWait()
        pg.hotkey('winleft')
        pg.write('spyder', interval=0.25)
        pg.hotkey('enter')
        
        
    if "открой spider" in task:
        text = "смнени раскладку дебббб, сменил а а а а"
        start.say(text)
        start.runAndWait()
        pg.hotkey('winleft')
        pg.write('spyder', interval=0.25)
        pg.hotkey('enter')
        
        
    if "закрой окно" in task:
        text = "может сам, а а а а а"
        start.say(text)
        start.runAndWait()
        pg.hotkey('altleft', 'f4')
        
        
    if "пора спать" in task:
        text = "ну, ладно"
        start.say(text)
        start.runAndWait()
        pg.hotkey('winleft')
        pg.click(22, 1027)
        pg.moveTo(99, 908, 1)
        pg.click(99, 908)
        pg.click(99, 908)
          
        
    if "сверни все окна" in task:
        text = "может сам, а а а а а"
        start.say(text)
        start.runAndWait()
        pg.hotkey('winleft', 'd')
    
    
    if "открой google" in task:
        text = "смнени раскладку деб б б б, сменил а а а а"
        start.say(text)
        start.runAndWait()
        pg.hotkey('winleft')
        pg.write('google', interval=0.25)
        pg.hotkey('enter')
    



while True:
    request(listen())
    

 



