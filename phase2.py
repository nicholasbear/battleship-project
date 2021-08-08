import ai
import enemyboard
import random
import tkinter
from tkinter import *

import tkinter.messagebox as msgbox

class page2:
<<<<<<< HEAD
    def __init__(self):
        self.window=Tk()
=======

    def __init__(self):
        self.window=tkinter.Tk()
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
        self.window.title("Battleship by 머저리")
        self.window.geometry("1220x640+100+100")

        me = Label(self.window,text='Player',width = 4, height = 2, fg="black")                        #위에 타이틀
        me.place(x=220,y=0,width=40,height=40)
        log = Label(self.window,text='log',width = 4, height = 2, fg="black")                          #위에 타이틀
        log.place(x=580,y=0,width=40,height=40)
        com = Label(self.window,text='Com',width = 4, height = 2, fg="black")
        com.place(x=940,y=0,width=40,height=40)

        mboard=[[0 for col in range(10)] for row in range(10)]
<<<<<<< HEAD
        eboard=enemyboard.Enemyboard()
=======
        eboard= enemyboard.Enemyboard()
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
        eboard.clear()
        eboard.get_ship(4)
        eboard.get_ship(3)
        eboard.get_ship(2)

        mshowboard=ai.aimove()

        eshowboard=[[0 for col in range(10)] for row in range(10)]

        

        myx=0
        myy=0
        ex=0
        ey=0

        self.window.mainloop()

        while(mshowboard.findboat!=0):
            num=0
            self.mshowboardgui(mshowboard,self.window)
            self.eshowboardgui(eshowboard,self.window)
            self.ifeboatcrashed(eshowboard,self.window)
            self.ifmyboatcrashed(mshowboard.mshowboard,self.window)
            self.log(self.window,myx,myy,ex,ey,num)
            
            if mshowboard.findaddboat()==0:
                root = Tk()
                root.withdraw()
                msgbox.showinfo("패배했습니다")
                break
            elif mshowboard.findaddboat()==0:
                root = Tk()
                root.withdraw()
                msgbox.showinfo("승리했습니다")
                break

            self.mymoveinput(self.window,eshowboard,eboard.enemy_board)                           #내가 둔수
            mshowboard.initboat()                                                                 #적이 둔수
            mshowboard.findboat()
            mshowboard.aimove(mboard.myboard)
            myx=mshowboard.xpos
            myy=mshowboard.ypos
            
            num+=1  
        self.window.mainloop()                   




<<<<<<< HEAD
    def mshowboardgui(self,mshowboard,window):   
        for i in range(10):                                                                       # 보드 표시부분
=======
    def mshowboardgui(self,mshowboard,window):                                                     #내보드 출력하는 함수
        for i in range(10):                                                                      
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
            for j in range(10):
                if mshowboard.mshowboard[i][j]==0:                 
                    test = Label(window,width = 4, height = 2, relief="solid", bg = "lavender")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==1:
                    test = Label(window,width = 4, height = 2, relief="solid", bg = "black")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==2:
                    test = Label(window,text='2',width = 4, height = 2, relief="solid", bg = "yellow")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==3:
                    test = Label(window,text='3',width = 4, height = 2, relief="solid", bg = "red")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==4:
                    test = Label(window,text='4',width = 4, height = 2, relief="solid", bg = "blue")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)

<<<<<<< HEAD
    def eshowboardgui(self,eshowboard,window):
=======
    def eshowboardgui(self,eshowboard,window):                                                     #적 보드 출력하는 함수
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
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


<<<<<<< HEAD
    def ifmyboatcrashed(self,mshowboard,window):
=======
    def ifmyboatcrashed(self,mshowboard,window):                                               #격추됬는지 확인하는 함수 내거
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
        temp = Label(window,text='2번배',width = 4, height = 2)
        temp.place(x=40,y=480)
        if self.countboat(2,mshowboard)==2:
            shotboat2 = Label(window,text='격추됨',width = 4, height = 2)
            shotboat2.place(x=40,y=520)
        temp = Label(window,text='3번배',width = 4, height = 2)
        temp.place(x=200,y=480)
        if self.countboat(3,mshowboard)==3:
            shotboat3 = Label(window,text='격추됨',width = 4, height = 2)
            shotboat3.place(x=200,y=520)
        temp = Label(window,text='4번배',width = 4, height = 2)
        temp.place(x=360,y=480)
        if self.countboat(4,mshowboard)==4:
            shotboat4 = Label(window,text='격추됨',width = 4, height = 2)
            shotboat4.place(x=360,y=520)

<<<<<<< HEAD
    def ifeboatcrashed(self,eshowboard,window):
=======
    def ifeboatcrashed(self,eshowboard,window):                                               #격추됬는지 확인하는 함수 적
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
        temp = Label(window,text='2번배',width = 4, height = 2)
        temp.place(x=800,y=480)
        if self.countboat(2,eshowboard)==2:
            shotboat2 = Label(window,text='격추됨',width = 4, height = 2)
            shotboat2.place(x=800,y=520)
        temp = Label(window,text='3번배',width = 4, height = 2)
        temp.place(x=960,y=480)
        if self.countboat(3,eshowboard)==3:
            shotboat3 = Label(window,text='격추됨',width = 4, height = 2)
            shotboat3.place(x=960,y=520)
        temp = Label(window,text='4번배',width = 4, height = 2)
        temp.place(x=1120,y=480)
        if self.countboat(4,eshowboard)==4:
            shotboat4 = Label(window,text='격추됨',width = 4, height = 2)
            shotboat4.place(x=1120,y=520)

<<<<<<< HEAD
        ###################################################################
        #로그부분

    def log(self,window,myx,myy,ex,ey,num):
=======
    def log(self,window,myx,myy,ex,ey,num):                                                 #로그창
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
        logbox=Listbox(window,width=34,height=22)
        logbox.place(x=480,y=40)
        scrollbar=Scrollbar(window,orient="vertical")
        scrollbar.config(command=logbox.yview)
        scrollbar.pack(side="right",fill="y")
        logbox.config(yscrollcommand=scrollbar.set)
        if num!=0:
            logbox.insert("user "+ex+","+ey+"에놓음 "+num+"회")
            logbox.insert("user "+myx+","+myy+"에놓음 "+num+"회")

<<<<<<< HEAD
page2()
=======
    def countboat(self,boatnum,board):                                                     #몇번배가 몇개있는지 세는 함수
        num=0
        for i in range(10):
            for j in range(10):
                if board[i][j]==boatnum:
                    num+=1
        return num
    
    def mymoveinput(self,window,eshowboard,eboard):                                        #내가 쏘는 좌표 입력하는 함수
        global ex
        global ey
        temp = Label(window, text = "행 : ",width = 4, height = 2)
        temp.place(x = 500, y = 480)
        rowinput = Entry(window, width = 4)
        rowinput.place(x = 540, y = 480)

        temp = Label(window, text = "열 : ",width = 4, height = 2)
        temp.place(x = 620, y = 480)
        columninput = Entry(window, width = 4)
        columninput.place(x = 660, y = 480)

        ex=columninput.get()
        ey=rowinput.get()
        ex=int(float(ex))-1
        ey=11-int(float(ey))
        

        firebutton = Button(window, text = "가즈아~", bg = "alice blue", command = self.moveok(row,column,eshowboard,eboard))
        firebutton.place(x = 560, y = 520)
        
    def moveok(self,row,column,eshowboard,eboard):                                         #이점에 쏠수 있는지 검사하는 함수 
        if self.movevalid(row,column,eshowboard)==True :
            if eboard[row][column]==0:
                eshowboard[row][column]==1
            else :
                eshowboard[row][column]==eboard[row][column]
        else:
            self.mymoveinput()


    def movevalid(self,xpos,ypos,mshowboard):                                                  #입력하려는 점 확인하는 함수
            if xpos>=0 and xpos <=9 and ypos>=0 and ypos<=9 and mshowboard[xpos][ypos]==0:
                return True
            else :
                return False

damn=page2()
>>>>>>> 4accfb2bdc829638014a3fcac9e3dd0cc287a3e3
