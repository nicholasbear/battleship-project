#ai 부분
import random

def initboard():                                                           #따로 보드하나 만듬
    newaiboard= [[0 for col in range(10)] for row in range(10)]


def findboat(mshowboard):                                                  #일단 발견 보트 개수 파악
    boat2=0
    boat3=0
    boat4=0

    for i in mshowboard:
        for j in range(10):
            if mshowboard[i][j]==2:
                boat2+=1
            elif mshowboard[i][j]==3:
                boat3+=1
            elif mshowboard[i][j]==4:
                boat4+=1

def findaddboat():                                                         #어떤 보트 추가하는건지 확인       
    if findboat.boat2==0 and findboat.boat3==0 and findboat.boat4==0:       #랜덤으로 추가해야됨
        return 1
    elif findboat.boat2==1:                                                 #2번배
        return 2
    elif findboat.boat3<3 and findboat.boat3>0:
        return 3
    elif findboat.boat4<4:
        return 4
    else:
        return 0

def movevalid(xpos,ypos,board):                                             #입력하려는 점 확인하는 함수
    if xpos>=0 and xpos <=9 and ypos>=0 and ypos<=9 and board[xpos][ypos]==0:
        return True
    else :
        return False

def findpos(board,findaddboat):                                            #배치 확인          num은 몇번 배인지 boatnum은 그 배가 현재 몇번 쏴줬는지 return 값은 입력할 좌표
    if findaddboat==2:
        boatnum=findboat.boat2
    if findaddboat==3:
        boatnum=findboat.boat3
    if findaddboat==4:
        boatnum=findboat.boat4

    if boatnum==1:       
        for i in board:
            for j in i:
                if board[i][j]==findaddboat:
                    if movevalid(i,j+1,board)==True:
                        return i*10+j
                    elif movevalid(i+1,j,board)==True:
                        return i*10+j
                    elif movevalid(i,j-1,board)==True:
                        return i*10+j
                    elif movevalid(i-1,j,board)==True:
                        return i*10+j
    elif boatnum==2:
        a=0
        temp=[0,0,0,0]
        for i in board:
            for j in i:
                if board[i][j]==findaddboat:
                    a+=1
                    if a==1:
                        temp[0]=i
                        temp[1]=j
                    if a==2:
                        temp[2]=i
                        temp[3]=j
                        break
        if temp[0]==temp[2]:
            if movevalid(temp[0],temp[1]-1,board)==True:
                return temp[0]*10+temp[1]-1
            else:
                return temp[0]*10+temp[1]+2
        else:
            if movevalid(temp[0]-1,temp[1],board)==True:
                return 10*(temp[0]-1)+temp[1]
            else :
                return 10*(temp[0]+2)+temp[1]

    else:
        a=0
        temp=[0,0,0,0]
        for i in board:
            for j in i:
                if board[i][j]==findaddboat:
                    a+=1
                    if a==1:
                        temp[0]=i
                        temp[1]=j
                    if a==2:
                        temp[2]=i
                        temp[3]=j
                        break
        if temp[0]==temp[2]:
            if movevalid(temp[0],temp[1]-1,board)==True:
                return temp[0]*10+temp[1]-1
            else:
                return temp[0]*10+temp[1]+3
        else:
            if movevalid(temp[0]-1,temp[1],board)==True:
                return 10*(temp[0]-1)+temp[1]
            else :
                return 10*(temp[0]+3)+temp[1]

def aimove(myboard,mshowboard):
    if findaddboat==1:                          #보트 찾은 거 없을때 111111111111
        xpos=random.randrange(0,10)
        ypos=random.randrange(0,10)
        while(mshowboard[xpos][ypos]!=0):         #쏘는 좌표 정하기
            xpos=random.randrange(0,10)
            ypos=random.randrange(0,10)

        if myboard[xpos][ypos]==0:             #보드 변경 해주기
            mshowboard[xpos][ypos]=1
        else:
            mshowboard[xpos][ypos]=myboard[xpos][ypos]
    
    elif findaddboat==2:                           #2번 보트 찾았을때
        xpos=findpos(mshowboard,2)/10
        ypos=findpos(mshowboard,2)*10
        mshowboard[xpos][ypos]=2
    
    elif findaddboat==2:                           #3번 보트 찾았을때
        xpos=findpos(mshowboard,3)/10
        ypos=findpos(mshowboard,3)*10
        mshowboard[xpos][ypos]=3
    else:                                          #4번 보트 찾았을때
        xpos=findpos(mshowboard,4)/10
        ypos=findpos(mshowboard,4)*10
        mshowboard[xpos][ypos]=4