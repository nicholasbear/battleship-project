import ai
import enemyboard
import random
import phase1
import tkinter
from tkinter import *

import tkinter.messagebox as msgbox

class page2:
    
    def __init__(self):

        mboard= [[0 for col in range(10)] for row in range(10)]
        mboard[0][1]=2
        mboard[0][2]=2
        mboard[1][1]=3
        mboard[1][2]=3
        mboard[1][3]=3
        mboard[2][1]=4
        mboard[2][2]=4
        mboard[2][3]=4
        mboard[2][4]=4

        eboard= enemyboard.Enemyboard()
        eboard.clear()
        eboard.get_ship(4)
        eboard.get_ship(3)
        eboard.get_ship(2)

        mshowboard=ai.aimove()

        eshowboard=[[0 for col in range(10)] for row in range(10)]

        myx=0       #적이둔수
        myy=0
        ex='0'        #내가둔수
        ey='0'

        while(mshowboard.findboat!=0):
            self.window=tkinter.Tk()
            self.window.title("Battleship by 머저리")
            self.window.geometry("1220x640+100+100")

            me = Label(self.window,text='Player',width = 4, height = 2, fg="black")                        #위에 타이틀
            me.place(x=220,y=0,width=40,height=40)
            log = Label(self.window,text='log',width = 4, height = 2, fg="black")                          #위에 타이틀
            log.place(x=580,y=0,width=40,height=40)
            com = Label(self.window,text='Com',width = 4, height = 2, fg="black")
            com.place(x=940,y=0,width=40,height=40)
            temp1 = Label(self.window, text = "행 : ",width = 4, height = 2)
            temp1.place(x = 500, y = 480)
            temp2 = Label(self.window, text = "열 : ",width = 4, height = 2)
            temp2.place(x = 620, y = 480)
            num=0
            self.mshowboardgui(mshowboard)                                            
            self.eshowboardgui(eshowboard)
            self.ifeboatcrashed(eshowboard)
            self.ifmyboatcrashed(mshowboard.mshowboard)
            self.log(myx,myy,ex,ey,num)
            
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

            rowinput = Entry(self.window, width = 4)
            rowinput.place(x = 540, y = 480)
            columninput = Entry(self.window, width = 4)
            columninput.place(x = 660, y = 480)
            firebutton = Button(self.window, text = "가즈아~", bg = "alice blue", command = lambda: self.firecommand(rowinput,columninput,eshowboard,eboard.enemy_board))
            firebutton.place(x = 560, y = 520)           
            self.window.mainloop()

            mshowboard.initboat()                                                                 
            mshowboard.findboat(mshowboard.mshowboard)
            mshowboard.aimove(mboard)
            myx=mshowboard.xpos
            myy=mshowboard.ypos
            
            num+=1
        self.window.mainloop()
        print("done")
   
    def mshowboardgui(self,mshowboard):                                                     #내보드 출력하는 함수
        for i in range(10):                                                                      
            for j in range(10):
                if mshowboard.mshowboard[i][j]==0:                 
                    test = Label(self.window,width = 4, height = 2, relief="solid", bg = "lavender")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==1:
                    test = Label(self.window,width = 4, height = 2, relief="solid", bg = "black")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==2:
                    test = Label(self.window,text='2',width = 4, height = 2, relief="solid", bg = "yellow")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==3:
                    test = Label(self.window,text='3',width = 4, height = 2, relief="solid", bg = "red")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)
                elif mshowboard.mshowboard[i][j]==4:
                    test = Label(self.window,text='4',width = 4, height = 2, relief="solid", bg = "blue")
                    test.place(x=40*i+40,y=40*j+40,width=40,height=40)

    def eshowboardgui(self,eshowboard):                                                     #적 보드 출력하는 함수
        for i in range(10):                                                         
            for j in range(10):
                if eshowboard[i][j]==0:
                    test = Label(self.window,width = 4, height = 2, relief="solid", bg = "lavender")
                    test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
                elif eshowboard[i][j]==1:
                    test = Label(self.window,width = 4, height = 2, relief="solid", bg = "black")
                    test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
                elif eshowboard[i][j]==2:
                    test = Label(self.window,text='2',width = 4, height = 2, relief="solid", bg = "yellow")
                    test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
                elif eshowboard[i][j]==3:
                    test = Label(self.window,text='3',width = 4, height = 2, relief="solid", bg = "red")
                    test.place(x=40*(i+19),y=40*j+40,width=40,height=40)
                elif eshowboard[i][j]==4:
                    test = Label(self.window,text='4',width = 4, height = 2, relief="solid", bg = "blue")
                    test.place(x=40*(i+19),y=40*j+40,width=40,height=40)

    def ifmyboatcrashed(self,mshowboard):                                                   #격추됬는지 확인하는 함수 내거
        temp = Label(self.window,text='2번배',width = 4, height = 2)
        temp.place(x=40,y=480)
        if self.countboat(2,mshowboard)==2:
            shotboat2 = Label(self.window,text='격추됨',width = 4, height = 2)
            shotboat2.place(x=40,y=520)
        temp = Label(self.window,text='3번배',width = 4, height = 2)
        temp.place(x=200,y=480)
        if self.countboat(3,mshowboard)==3:
            shotboat3 = Label(self.window,text='격추됨',width = 4, height = 2)
            shotboat3.place(x=200,y=520)
        temp = Label(self.window,text='4번배',width = 4, height = 2)
        temp.place(x=360,y=480)
        if self.countboat(4,mshowboard)==4:
            shotboat4 = Label(self.window,text='격추됨',width = 4, height = 2)
            shotboat4.place(x=360,y=520)

    def ifeboatcrashed(self,eshowboard):                                                    #격추됬는지 확인하는 함수 적
        temp = Label(self.window,text='2번배',width = 4, height = 2)
        temp.place(x=800,y=480)
        if self.countboat(2,eshowboard)==2:
            shotboat2 = Label(self.window,text='격추됨',width = 4, height = 2)
            shotboat2.place(x=800,y=520)
        temp = Label(self.window,text='3번배',width = 4, height = 2)
        temp.place(x=960,y=480)
        if self.countboat(3,eshowboard)==3:
            shotboat3 = Label(self.window,text='격추됨',width = 4, height = 2)
            shotboat3.place(x=960,y=520)
        temp = Label(self.window,text='4번배',width = 4, height = 2)
        temp.place(x=1120,y=480)
        if self.countboat(4,eshowboard)==4:
            shotboat4 = Label(self.window,text='격추됨',width = 4, height = 2)
            shotboat4.place(x=1120,y=520)

    def log(self,myx,myy,ex,ey,num):                                                        #로그창
        logbox=Listbox(self.window,width=34,height=22)
        logbox.place(x=480,y=40)
        scrollbar=Scrollbar(self.window,orient="vertical")
        scrollbar.config(command=logbox.yview)
        scrollbar.pack(side="right",fill="y")
        logbox.config(yscrollcommand=scrollbar.set)
        if num!=0:
            logbox.insert("user "+ex+","+ey+"에놓음 "+num+"회")
            logbox.insert("user "+myx+","+myy+"에놓음 "+num+"회")

    def countboat(self,boatnum,board):                                                      #몇번배가 몇개있는지 세는 함수
        num=0
        for i in range(10):
            for j in range(10):
                if board[i][j]==boatnum:
                    num+=1
        return num
      
    def firecommand(self,rowinput,columninput,eshowboard,eboard):                                             #버튼 커맨드
      global ex
      global ey 
      ex=self.entryvalue(columninput)-1
      ey=10-self.entryvalue(rowinput)
      
      if ex>=0 and ex<=9 and ey>=0 and ey<=9:
        if eshowboard[ex][ey]!=0:
            print("Problem")
            root = Tk()
            root.withdraw()
            msgbox.showinfo("중복 입력했습니다 다시 입력하세요")
            self.firecommand(self,rowinput,columninput,eshowboard,eboard)
        print("good")
        if eboard[ex][ey]==0:
            eshowboard[ex][ey]=1
        else:
            eshowboard[ex][ey]=eboard[ex][ey]
         
      else:
        print("Problem")
        root = Tk()
        root.withdraw()
        msgbox.showinfo("잘못 입력했습니다 다시 입력하세요")
        self.firecommand(self,rowinput,columninput,eshowboard,eboard)
             
    def entryvalue(self,entry):                                                             #Entry 받는값 교정하는 함수
        value=entry.get()
        try:
            return int(value)
        except ValueError:
            print("wrong value")
            return 0

damn=page2()
