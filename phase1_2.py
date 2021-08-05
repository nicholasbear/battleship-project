from tkinter import *
from tkinter import font

class phase1:
    arr=[[0 for i in range(10)]for i in range(10)]
    myboard = [[0 for i in range(10)]for i in range(10)]

    def placeship(self,shipsize):
        col = int(self.entry1.get())-1       #x좌표는 colon
        if col > 11 - shipsize or col < 0:
            self.label5.config(text = "배의 크기 {} 를 생각해서 X좌표를 정해주세요.".format(shipsize), fg = "red")
            return

        row = 10 - int(self.entry2.get())    #y좌표는 11-row
        if row > 10 or row < shipsize - 1:
            self.label5.config(text = "배의 크기 {} 를 생각해서 Y좌표를 정해주세요.".format(shipsize), fg = "red")
            return

        dir = int(self.entry3.get())
        if dir > 2 or dir < 1:
            self.label5.config(text = "가로 = 1, 세로 = 2   //   1, 2 중 하나를 눌러주세요.", fg = "red")
            return

        sum = 0
        if dir == 1: #배가 가로로 놓임
            for i in range (shipsize):
                sum += self.myboard[row][col+i]
            if sum == 0:
                for i in range (shipsize):
                    self.myboard[row][col+i] = shipsize
                    self.arr[row][col+i].config(text = shipsize)
            else:
                self.label5.config(text = "기존의 배와 겹칩니다. 다시 입력해주세요.")

        if dir == 2: #배가 세로로 놓임
            for i in range (shipsize):
                sum += self.myboard[row-i][col]
            if sum == 0:
                for i in range (shipsize):
                    self.myboard[row-i][col] = shipsize
                    self.arr[row-i][col].config(text = shipsize)
            else:
                self.label5.config(text = "기존의 배와 겹칩니다. 다시 입력해주세요.")    

    def clear(self):
        for i in range(10):
            for j in range(10):
                self.arr[i][j].config(text = 0)
                self.myboard[i][j] = 0

    window=Tk()
    window.title("phase1")
    window.geometry('500x360')
    window.config(bg = "ghost white")

    font1=font.Font(size=15)

    row_index = 0
    col_index = 0
    for i in range(10):
        for j in range(10):
            arr[i][j] = Label(window, text = myboard[i][j], width = 2, height = 1, font = font1, relief="solid", bg = "lavender")
            arr[i][j].place(x = 25*(j+1), y = 25*(i+1))

    label1 = Label(window, text = "X : ",bg = "ghost white")
    label1.place(x = 300, y = 40)
    entry1 = Entry(window, width = 5)
    entry1.place(x = 330, y = 40)

    label2 = Label(window, text = "Y : ",bg = "ghost white")
    label2.place(x = 400, y = 40)
    entry2 = Entry(window, width = 5)
    entry2.place(x = 430, y = 40)

    label3 = Label(window, text = "가로/세로 : ",bg = "ghost white")
    label3.place(x = 300, y = 80)
    entry3 = Entry(window, width = 5)
    entry3.place(x = 370, y = 80)

    label4 = Label(window, text = "놓을 배의 시작부분의 X좌표, Y좌표, 가로/세로를 입력한 후 배 크기 버튼을 누르세요.",bg = "ghost white")
    label4.place(x = 25, y = 290)

    label5 = Label(window, text = "", bg = "ghost white", fg = "red")
    label5.place(x = 25, y = 320)

    button1 = Button(window, text = "2칸 배", bg = "alice blue", command = lambda : placeship(2))
    button1.place(x = 310, y = 120)

    button2 = Button(window, text = "3칸 배", bg = "honeydew", command = lambda : placeship(3))
    button2.place(x = 310, y = 160)

    button3 = Button(window, text = "4칸 배", bg = "ivory", command = lambda : placeship(4))
    button3.place(x = 310, y = 200)

    button4 = Button(window, text = "초기화", command = clear)
    button4.place(x = 310, y = 240)

    button5 = Button(window, text = "완료") #command = phase2
    button5.place(x = 430, y = 240)

    window.mainloop()