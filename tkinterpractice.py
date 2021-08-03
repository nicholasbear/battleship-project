from tkinter import *
import random as rd

won = 0
count = 0

def reload():
    global won, count
    a = entry.get()
    won += int(a)
    count = 0
    label3.config(text = "남은 금액 : {}원".format(won))
    label2.config(text = "")
    result.config(text = "")
    
def gamble():
    global won, count
    a = rd.randint(0,1)
    if won > 0:
        count += 1
        if a == 0:
            won += 100
            label2.config(text = "앞면 / 100원을 얻습니다. / {}회 실행".format(count))
            label3.config(text = "남은 금액 : {}원".format(won))
        elif a == 1:
            won -= 150
            label2.config(text = "뒷면 / 150원을 잃습니다. / {}회 실행".format(count))
            label3.config(text = "남은 금액 : {}원".format(won))
        if won <= 0:
            won = 0
            label3.config(text = "남은 금액 : 0원")
            result.config(text = "남은 금액이 없습니다. / {}회 실행".format(count))
    else:
        label2.config(text = "돈을 충전하세요.")
        result.config(text = "남은 금액이 없습니다. / {}회 실행".format(count))
        
window = Tk()
window.title("동전 던지기")
window.geometry('240x240') 

label1 = Label(text = '금액 입력 : ')
label1.place(x = 10, y = 10)

entry = Entry(window, width = 20)
entry.place(x = 80, y = 10)

button1 = Button(window, text='금액 충전', command = reload)
button1.place(x = 40, y = 50)

button2 = Button(window, text='동전 던지기', command = gamble)
button2.place(x = 130, y = 50)

label2 = Label(text = "")
label2.place(x = 20, y = 100)

label3 = Label(text = "남은 금액 : ")
label3.place(x = 40, y = 140)

result = Label(text = "")
result.place(x = 20, y = 180)

window.mainloop()