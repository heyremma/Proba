from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame#для работы со звуком

window=Tk()
window.title("Напоминание")
l=Label(text="Установите напоминание")
l.pack(pady=10)
set_button=Button(text="Установить напоминание", command=set)
set_button.pack()

wondow.mainloop()
