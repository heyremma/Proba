from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame#для работы со звуком

t=0

def set():
    global t
    rem=sd.askstring("Время напоминания", "Введите время напоминания в формате hh:mm")
    if rem:#если переменная rem не пустая
        try:
            hour=int(rem.split(":")[0])#сплит по символу :, по умолч. по пробелу и берем часть с индексом ноль, то есть первую
            minute=int(rem.split(":")[1])#то же самое, но по индексу 1, то есть вторая часть
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute)#заменяем параметры на введенные переменные
            print(dt)
            t=dt.timestamp()
            print(t)
            text=sd.askstring("Текст напоминания","Введите текст напоминания")
            label.config(text=f"Напоминание на {hour:02}:{minute:02} с текстом {text}")
        except Exception as e:
            mb.showerror("Ошибка!",f"Произошла ошибка {e}")

def check():
    global t
    if t:#если переменная т существует
        now=time.time()
        if now>=t:
            play_snd()
            t=0
    window.after(10000, check)#проверка раз в 10 секунд


def play_snd():
    pygame.mixer.init()#инициализируем миксер, который играет музыку
    pygame.mixer.music.load("rem.mp3")#загружаем музыку, файл должен быть в папке проекта (C:\Users\User\PycharmProjects\Project3)
    pygame.mixer.music.play()#включаем музыку НЕ ХОЧЕТ РАБОТАТЬ!!!!


window=Tk()
window.title("Напоминание")
label=Label(text="Установите напоминание")
label.pack(pady=10)
set_button=Button(text="Установить напоминание", command=set)
set_button.pack()

check()

window.mainloop()
