import ai
import enemyboard
import myboard
import mymove
import phase1
import phase2
import newmyboard
import tkinter.messagebox as msgbox
import tkinter
from tkinter import *
import newmymove

##### 첫번쨰 페이지














#### 두번째 페이지                                                      #보드 4개 먼저 초기화
mboard=
eboard= enemyboard.Enemyboard()
eboard.clear()
eboard.get_ship(4)
eboard.get_ship(3)
eboard.get_ship(2)
mshowboard=ai.aimove()   
eshowboard=[[0 for col in range(10)] for row in range(10)]
###
#윈도우 및 위에 글자들
window=tkinter.Tk()
window.title("Battleship by 머저리")
window.geometry("1220x640+100+100")
window.resizable(False, False)
me = Label(window,text='Player',width = 4, height = 2, fg="black")                        #위에 타이틀
me.place(x=220,y=0,width=40,height=40)
log = Label(window,text='log',width = 4, height = 2, fg="black")                          #위에 타이틀
log.place(x=580,y=0,width=40,height=40)
com = Label(window,text='Com',width = 4, height = 2, fg="black")
com.place(x=940,y=0,width=40,height=40)

while(ai.findboat!=0):
    phase2.show2(eshowboard,mshowboard.mshowboard)
    
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

    newmymove.mymoveinput(window,eshowboard,eboard)                                    #내가 둔수
    mshowboard.initboat()                                                              #적이 둔수
    mshowboard.findboat()
    mshowboard.aimove(mboard)                     
