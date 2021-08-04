import ai
import enemyboard
import random
import tkinter
from tkinter import *

def show2():
    window=tkinter.Tk()
    window.title("Battleship by 머저리")
    window.geometry("1200x640+100+100")
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

    mboard= [[0 for col in range(10)] for row in range(10)]                         #myboard 설정함

    eshowboard= [[0 for col in range(10)] for row in range(10)]                     #display되는 상대 보드
    mshowboard= [[0 for col in range(10)] for row in range(10)]                     #display되는 내 보드



    #display 되는 부분 //////////////////////////////////////////////////////////////////////////////////////////
    me = Label(window,text='Me',width = 4, height = 2, fg="black")                        #위에 타이틀
    me.place(x=220,y=0,width=40,height=40)
    log = Label(window,text='log',width = 4, height = 2, fg="black")                        #위에 타이틀
    log.place(x=580,y=0,width=40,height=40)
    com = Label(window,text='Com',width = 4, height = 2, fg="black")
    com.place(x=940,y=0,width=40,height=40)
    ##########################################
    for i in range(10):                                                                     # 보드 표시부분
        for j in range(10):
            if mshowboard[i][j]==0:
                test = Label(window,width = 4, height = 2, relief="solid", bg = "lavender")
                test.place(x=40*i+40,y=40*j+40,width=40,height=40)
            elif mshowboard[i][j]==1:
                test = Label(window,width = 4, height = 2, relief="solid", bg = "black")
                test.place(x=40*i+40,y=40*j+40,width=40,height=40)
            elif mshowboard[i][j]==2:
                test = Label(window,text='2',width = 4, height = 2, relief="solid", bg = "yellow")
                test.place(x=40*i+40,y=40*j+40,width=40,height=40)
            elif mshowboard[i][j]==3:
                test = Label(window,text='3',width = 4, height = 2, relief="solid", bg = "red")
                test.place(x=40*i+40,y=40*j+40,width=40,height=40)
            elif mshowboard[i][j]==4:
                test = Label(window,text='4',width = 4, height = 2, relief="solid", bg = "blue")
                test.place(x=40*i+40,y=40*j+40,width=40,height=40)

    for i in range(10):                                                         
        for j in range(10):
            if eshowboard[i][j]==0:
                test = Label(window,width = 4, height = 2, relief="solid", bg = "lavender")
                test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
            elif eshowboard[i][j]==1:
                test = Label(window,width = 4, height = 2, relief="solid", bg = "black")
                test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
            elif eshowboard[i][j]==2:
                test = Label(window,text='2',width = 4, height = 2, relief="solid", bg = "yellow")
                test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
            elif eshowboard[i][j]==3:
                test = Label(window,text='3',width = 4, height = 2, relief="solid", bg = "red")
                test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
            elif eshowboard[i][j]==4:
                test = Label(window,text='4',width = 4, height = 2, relief="solid", bg = "blue")
                test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
    ###########################################################
    #격추됬는지 표시부분
    temp = Label(window,text='2번배',width = 4, height = 2)
    temp.place(x=40,y=480)
    shotboat2 = Label(window,text='?',width = 4, height = 2)
    shotboat2.place(x=40,y=520)
    temp = Label(window,text='3번배',width = 4, height = 2)
    temp.place(x=200,y=480)
    shotboat3 = Label(window,text='?',width = 4, height = 2)
    shotboat3.place(x=200,y=520)
    temp = Label(window,text='4번배',width = 4, height = 2)
    temp.place(x=360,y=480)
    shotboat4 = Label(window,text='?',width = 4, height = 2)
    shotboat4.place(x=360,y=520)
    temp = Label(window,text='2번배',width = 4, height = 2)
    temp.place(x=800,y=480)
    shotboat2 = Label(window,text='?',width = 4, height = 2)
    shotboat2.place(x=800,y=520)
    temp = Label(window,text='3번배',width = 4, height = 2)
    temp.place(x=960,y=480)
    shotboat3 = Label(window,text='?',width = 4, height = 2)
    shotboat3.place(x=960,y=520)
    temp = Label(window,text='4번배',width = 4, height = 2)
    temp.place(x=1120,y=480)
    shotboat4 = Label(window,text='?',width = 4, height = 2)
    shotboat4.place(x=1120,y=520)

    '''
    #############################################################
    #행열 입력하는부분
    temp = Label(window, text = "행 : ",width = 4, height = 2)
    temp.place(x = 500, y = 480)
    rowinput = Entry(window, width = 4)
    rowinput.place(x = 540, y = 480)

    temp = Label(window, text = "열 : ",width = 4, height = 2)
    temp.place(x = 620, y = 480)
    columninput = Entry(window, width = 4)
    columninput.place(x = 660, y = 480)

    firebutton = Button(window, text = "가즈아~", bg = "alice blue", command = ###############)
    firebutton.place(x = 560, y = 520)
    '''
    ###################################################################
    #로그부분

    logbox=Listbox(window,width=34,height=22)
    logbox.place(x=480,y=40)
    scrollbar=Scrollbar(window,orient="vertical")
    scrollbar.config(command=logbox.yview)
    scrollbar.pack(side="right",fill="y")
    logbox.config(yscrollcommand=scrollbar.set)
    for x in range(1000):
        logbox.insert(END, str(x))






    window.mainloop()
