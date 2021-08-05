from tkinter import *
from tkinter import font

class phase1:
    arr=[[0 for i in range(10)]for i in range(10)]
    myboard = [[0 for i in range(10)]for i in range(10)]

    def __init__(self):
        self.window=Tk()
        self.window.title("phase1")
        self.window.geometry('500x360')
        self.window.config(bg = "ghost white")

        self.font1=font.Font(size=15)

        for i in range(10):
            for j in range(10):
                self.arr[i][j] = Label(self.window, text = self.myboard[i][j], width = 2, height = 1, font = self.font1, relief="solid", bg = "lavender")
                self.arr[i][j].place(x = 25*(j+1), y = 25*(i+1))

        self.label1 = Label(self.window, text = "X : ",bg = "ghost white")
        self.label1.place(x = 300, y = 40)
        self.entry1 = Entry(self.window, width = 5)
        self.entry1.place(x = 330, y = 40)

        self.label2 = Label(self.window, text = "Y : ",bg = "ghost white")
        self.label2.place(x = 400, y = 40)
        self.entry2 = Entry(self.window, width = 5)
        self.entry2.place(x = 430, y = 40)

        self.label3 = Label(self.window, text = "가로/세로 : ",bg = "ghost white")
        self.label3.place(x = 300, y = 80)
        self.entry3 = Entry(self.window, width = 5)
        self.entry3.place(x = 370, y = 80)

        self.label4 = Label(self.window, text = "놓을 배의 시작부분의 X좌표, Y좌표, 가로/세로를 입력한 후 배 크기 버튼을 누르세요.",bg = "ghost white")
        self.label4.place(x = 25, y = 290)

        self.label5 = Label(self.window, text = "", bg = "ghost white", fg = "red")
        self.label5.place(x = 25, y = 320)

        self.button1 = Button(self.window, text = "2칸 배", bg = "alice blue", command = lambda : self.placeship(2))
        self.button1.place(x = 310, y = 120)

        self.button2 = Button(self.window, text = "3칸 배", bg = "honeydew", command = lambda : self.placeship(3))
        self.button2.place(x = 310, y = 160)

        self.button3 = Button(self.window, text = "4칸 배", bg = "ivory", command = lambda : self.placeship(4))
        self.button3.place(x = 310, y = 200)

        self.button4 = Button(self.window, text = "초기화", command = self.clear)
        self.button4.place(x = 310, y = 240)

        self.button5 = Button(self.window, text = "완료") #command = phase2
        self.button5.place(x = 430, y = 240)

        self.window.mainloop()

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

Phase1 = phase1()
Phase1.mainloop()