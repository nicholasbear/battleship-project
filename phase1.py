from tkinter import *
from tkinter import font

arr=[[[]for i in range(10)]for i in range(10)]
myboard = [[[]for i in range(10)]for i in range(10)]

window=Tk()
window.title("phase1")
window.geometry('500x310')
window.config(bg = "ghost white")

font1=font.Font(size=15)

row_index = 0
col_index = 0
for i in range(10):
    for j in range(10):
        arr[i][j] = Label(window, text = myboard[i][j], width = 2, height = 1, font = font1, relief="solid", bg = "lavender")
        arr[i][j].place(x = 25*(i+1), y = 25*(j+1))

label1 = Label(window, text = "행 : ",bg = "ghost white")
label1.place(x = 300, y = 40)
entry1 = Entry(window, width = 5)
entry1.place(x = 330, y = 40)

label2 = Label(window, text = "열 : ",bg = "ghost white")
label2.place(x = 400, y = 40)
entry2 = Entry(window, width = 5)
entry2.place(x = 430, y = 40)

label3 = Label(window, text = "가로/세로 : ",bg = "ghost white")
label3.place(x = 300, y = 80)
entry3 = Entry(window, width = 5)
entry3.place(x = 370, y = 80)

button1 = Button(window, text = "2칸 배", bg = "alice blue")
button1.place(x = 310, y = 120)

button2 = Button(window, text = "3칸 배", bg = "honeydew")
button2.place(x = 310, y = 160)

button3 = Button(window, text = "4칸 배", bg = "ivory")
button3.place(x = 310, y = 200)

button4 = Button(window, text = "초기화")
button4.place(x = 310, y = 240)

button5 = Button(window, text = "완료")
button5.place(x = 430, y = 240)

window.mainloop()  