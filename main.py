import ai
import enemyboard
import myboard
import mymove
import phase1
import phase2
import newmyboard
import tkinter.messagebox as msgbox
from tkinter import *

##### 첫번쨰 페이지














#### 두번째 페이지
mboard=
eboard= enemyboard.Enemyboard()
eboard.clear()
eboard.get_ship(4)
eboard.get_ship(3)
eboard.get_ship(2)
mshowboard=ai.initboard()   
eshowboard=ai.initboard()
###

while(ai.findboat!=0):
    phase2.show2(eshowboard,mshowboard)
    
    if ai.findaddboat(mshowboard)==0:
        root = Tk()
        root.withdraw()
        msgbox.showinfo("패배했습니다")
        break
    elif ai.findaddboat(eshowboard)==0:
        root = Tk()
        root.withdraw()
        msgbox.showinfo("승리했습니다")
        break

    eshowboard=                      #내가 둔수
    ai.aimove(mboard,mshowboard)     #적이 둔수
