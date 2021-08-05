import ai
import enemyboard
import random
import tkinter
import newmyboard
from tkinter import *

def mshowboardgui(mshowboard,window):   
    for i in range(10):                                                                       # 보드 표시부분
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

def eshowboardgui(eshowboard,window):
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


def ifmyboatcrashed(mshowboard,window):
    temp = Label(window,text='2번배',width = 4, height = 2)
    temp.place(x=40,y=480)
    if ai.findboat(mshowboard).boat2==2:
        shotboat2 = Label(window,text='격추됨',width = 4, height = 2)
        shotboat2.place(x=40,y=520)
    temp = Label(window,text='3번배',width = 4, height = 2)
    temp.place(x=200,y=480)
    if ai.findboat(mshowboard).boat3==3:
        shotboat3 = Label(window,text='격추됨',width = 4, height = 2)
        shotboat3.place(x=200,y=520)
    temp = Label(window,text='4번배',width = 4, height = 2)
    temp.place(x=360,y=480)
    if ai.findboat(mshowboard).boat4==4:
        shotboat4 = Label(window,text='격추됨',width = 4, height = 2)
        shotboat4.place(x=360,y=520)

def ifeboatcrashed(eshowboard,window):
    temp = Label(window,text='2번배',width = 4, height = 2)
    temp.place(x=800,y=480)
    if ai.findboat(eshowboard).boat2==2:
        shotboat2 = Label(window,text='격추됨',width = 4, height = 2)
        shotboat2.place(x=800,y=520)
    temp = Label(window,text='3번배',width = 4, height = 2)
    temp.place(x=960,y=480)
    if ai.findboat(eshowboard).boat3==3:
        shotboat3 = Label(window,text='격추됨',width = 4, height = 2)
        shotboat3.place(x=960,y=520)
    temp = Label(window,text='4번배',width = 4, height = 2)
    temp.place(x=1120,y=480)
    if ai.findboat(eshowboard).boat4==4:
        shotboat4 = Label(window,text='격추됨',width = 4, height = 2)
        shotboat4.place(x=1120,y=520)

    
    #############################################################
    #행열 입력하는부분 new my move에

    def mymoveinput():
        temp = Label(window, text = "행 : ",width = 4, height = 2)
        temp.place(x = 500, y = 480)
        rowinput = Entry(window, width = 4)
        rowinput.place(x = 540, y = 480)

        temp = Label(window, text = "열 : ",width = 4, height = 2)
        temp.place(x = 620, y = 480)
        columninput = Entry(window, width = 4)
        columninput.place(x = 660, y = 480)

        row=rowinput.get()
        column=columninput.get()

        firebutton = Button(window, text = "가즈아~", bg = "alice blue", command = moveok(row,column,eshowboard,eboard))
        firebutton.place(x = 560, y = 520)
    
    def moveok(row,column,eshowboard,eboard):       
        if ai.movevalid(row,column)==True and eshowboard[i][j]==0:
            if eboard[i][j]==0:
                eshowboard[i][j]==1
            else :
                 eshowboard[i][j]==eboard[i][j]
        else:
            mymoveinput()
    
    mymoveinput()
    ###################################################################
    #로그부분

    logbox=Listbox(window,width=34,height=22)
    logbox.place(x=480,y=40)
    scrollbar=Scrollbar(window,orient="vertical")
    scrollbar.config(command=logbox.yview)
    scrollbar.pack(side="right",fill="y")
    logbox.config(yscrollcommand=scrollbar.set)
    logbox.insert(, str(x))


