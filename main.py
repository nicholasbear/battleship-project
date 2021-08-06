import ai
import enemyboard
import phase1
import phase2
import mymove

import tkinter.messagebox as msgbox
import tkinter
from tkinter import *

##### 첫번쨰 페이지














#### 두번째 페이지                                                      #보드 4개 먼저 초기화
mboard=phase1.page1()

eboard= enemyboard.Enemyboard()
eboard.clear()
eboard.get_ship(4)
eboard.get_ship(3)
eboard.get_ship(2)

mshowboard=ai.aimove()

eshowboard=[[0 for col in range(10)] for row in range(10)]



