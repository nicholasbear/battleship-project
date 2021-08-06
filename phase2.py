import ai
import enemyboard
import mymove
import random
import phase1
import tkinter
from tkinter import *
import tkinter.messagebox as msgbox

class page2:

    def _init_(self):
        self.window=tkinter.Tk()
        self.window.title("Battleship by 머저리")
        self.window.geometry("1220x640+100+100")
        self.window.resizable(False, False)
        me = Label(self.window,text='Player',width = 4, height = 2, fg="black")                        #위에 타이틀
        me.place(x=220,y=0,width=40,height=40)
        log = Label(self.window,text='log',width = 4, height = 2, fg="black")                          #위에 타이틀
        log.place(x=580,y=0,width=40,height=40)
        com = Label(self.window,text='Com',width = 4, height = 2, fg="black")
        com.place(x=940,y=0,width=40,height=40)

        mboard=main.firstpage.myboard
        eboard= enemyboard.Enemyboard()
        eboard.clear()
        eboard.get_ship(4)
        eboard.get_ship(3)
        eboard.get_ship(2)

        mshowboard=ai.aimove()

        eshowboard=[[0 for col in range(10)] for row in range(10)]

        mymmove=mymove.mymove()

        while(mshowboard.findboat!=0):
            num=0
            self.mshowboardgui(mshowboard,self.window)
            self.eshowboardgui(eshowboard,self.window)
            self.ifeboatcrashed(eshowboard,self.window)
            self.ifmyboatcrashed(mshowboard,self.window)
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

            mymmove.mymoveinput(self.window,eshowboard,eboard.enemy_board)                          #내가 둔수
            mshowboard.initboat()                                                              #적이 둔수
            mshowboard.findboat()
            mshowboard.aimove(mboard.myboard)
            myx=mshowboard.xpos
            myy=mshowboard.ypos
            ex=mymmove.row
            ey=mymmove.column
            num+=1  
        self.window.mainloop()                   




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

        ###################################################################
        #로그부분

    def log(window,myx,myy,ex,ey,num):
        logbox=Listbox(window,width=34,height=22)
        logbox.place(x=480,y=40)
        scrollbar=Scrollbar(window,orient="vertical")
        scrollbar.config(command=logbox.yview)
        scrollbar.pack(side="right",fill="y")
        logbox.config(yscrollcommand=scrollbar.set)
        if num!=0:
            logbox.insert("user "+ex+","+ey+"에놓음 "+num+"회")
            logbox.insert("user "+myx+","+myy+"에놓음 "+num+"회")


