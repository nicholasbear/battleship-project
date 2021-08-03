from tkinter import *
from tkinter import font

window=Tk()  ## 첫번째 창을 띄우는 코드의 시작부분
window.geometry('480x300')

font1=font.Font(size=15)

Label(window, text = "난이도를 선택하세요").place(x = 170, y = 100)

button_easy = Button(window, text = "easy").place(x = 100, y = 170)
button_medium = Button(window, text = "medium",).place(x = 210, y = 170)
button_hard = Button(window, text = "hard",).place(x = 350, y = 170)

window.mainloop()