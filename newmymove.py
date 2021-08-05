import ai
import enemyboard
import random
import tkinter
import newmyboard
from tkinter import *

def mymoveinput(window,eshowboard,eboard):
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
    if movevalid(row,column,eshowboard)==True :
        if eboard[row][column]==0:
            eshowboard[row][column]==1
        else :
            eshowboard[row][column]==eboard[row][column]
    else:
        mymoveinput()

def movevalid(xpos,ypos,mshowboard):                                            #입력하려는 점 확인하는 함수
        if xpos>=0 and xpos <=9 and ypos>=0 and ypos<=9 and mshowboard[xpos][ypos]==0:
            return True
        else :
            return False