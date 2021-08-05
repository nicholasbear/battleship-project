import ai
import enemyboard
import myboard
import mymove
import phase1
import phase2
import newmyboard

##### 첫번쨰 페이지














#### 두번째 페이지

mshowboard=ai.initboard()   
eshowboard=ai.initboard()
###

while(ai.findboat!=0):
    phase2.show2(eshowboard,mshowboard)
    mshowboard=
    ai.aimove(myboard,mshowboard)
    if ai.findaddboat==0:
        print("you lost")
        break
    
