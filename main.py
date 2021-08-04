import ai
import enemyboard


import random
from tkinter import*


window=Tk()
window.title("Battleship by 머저리")
window.geometry("1000x600+100+100")
window.resizable(False, False)
'''
mb=Label(window, text="myboard", bg="yellow", fg="black")
mb.place(x=200, y=10)
eb=Label(window, text="enemyboard", bg="blue", fg="white")
eb.place(x=700, y=10)
'''
eboard=enemyboard.Enemyboard()       #enemyboard 설정함
eboard.clear()
eboard.get_ship(4)
eboard.get_ship(3)
eboard.get_ship(2)

mboard=                              #myboard 설정함

eshowboard= [[0 for col in range(10)] for row in range(10)]                     #display되는 상대 보드
mshowboard= [[0 for col in range(10)] for row in range(10)]                     #display되는 내 보드







#display 되는 부분 //////////////////////////////////////////////////////////////////////////////////////////

for i in range(10):                                                         
    for j in range(10):
        if mshowboard[i][j]==0:
            test = Label(window,width = 4, height = 2, relief="solid", bg = "lavender")
            test.grid(row = i, column=j)
        elif mshowboard[i][j]==1:
            test = Label(window,width = 4, height = 2, relief="solid", bg = "black")
            test.grid(row = i, column=j)
        if mshowboard[i][j]==2:
            test = Label(window,test='2',width = 4, height = 2, relief="solid", bg = "yellow")
            test.grid(row = i, column=j)
        if mshowboard[i][j]==3:
            test = Label(window,test='3',width = 4, height = 2, relief="solid", bg = "red")
            test.grid(row = i, column=j)
        if mshowboard[i][j]==4:
            test = Label(window,test='4',width = 4, height = 2, relief="solid", bg = "blue")
            test.grid(row = i, column=j)

for i in range(10):                                                         
    for j in range(10):
        if mshowboard[i][j]==0:
            test = Label(window,width = 4, height = 2, relief="solid", bg = "lavender")
            test.grid(row = i, column=j)
        elif mshowboard[i][j]==1:
            test = Label(window,width = 4, height = 2, relief="solid", bg = "black")
            test.grid(row = i, column=j)
        if mshowboard[i][j]==2:
            test = Label(window,test='2',width = 4, height = 2, relief="solid", bg = "yellow")
            test.grid(row = i, column=j)
        if mshowboard[i][j]==3:
            test = Label(window,test='3',width = 4, height = 2, relief="solid", bg = "red")
            test.grid(row = i, column=j)
        if mshowboard[i][j]==4:
            test = Label(window,test='4',width = 4, height = 2, relief="solid", bg = "blue")
            test.grid(row = i, column=j)       



window.mainloop()
