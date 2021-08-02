#ai 부분
import random

def initboard():                                                           #따로 보드하나 만듬
    aiboard= [[0 for col in range(10)] for row in range(10)]

def initnumboat():                                                         #격추시킨 수 초기화
    boat2=0
    boat3=0
    boat4=0

def findboat(board,boat2,boat3,boat4):                                     #일단 보트상황파악
    for i in board:
        for j in i:
            if board[i][j]==2:
                boat2+=1
            elif board[i][j]==3:
                boat3+=1
            elif board[i][j]==4:
                boat4+=1
        
    if boat2==0 and boat3==0 and boat4==0:
        return 1
    elif boat2<2:
        return 2
    elif boat3<3:
        return 3
    elif boat4<4:
        return 4
    else:
        print("You lost")
        return 0

def movevalid(xpos,ypos,board):                                            #입력하려는 점 확인하는 함수
    if xpos>=0 and xpos <=9 and ypos>=0 and ypos<=9 and board[xpos][ypos]==0:
        return True
    else :
        return False

def findpos(board,num,boatnum):                                            #배치 확인          num은 몇번 배인지 boatnum은 그 배가 현재 몇번 쏴줬는지 return 값은 입력할 좌표
    if boatnum==1:       
        for i in board:
            for j in i:
                if board[i][j]==num:
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
                if board[i][j]==num:
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
                if board[i][j]==num:
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

def aimove(myboard,aiboard,boat2,boat3,boat4):
    if findboat==1:                            #보트 찾은 거 없을때 111111111111
        xpos=random.randrange(0,10)
        ypos=random.randrange(0,10)
        while(aiboard[xpos][ypos]!=0):         #쏘는 좌표 정하기
            xpos=random.randrange(0,10)
            ypos=random.randrange(0,10)

        if myboard[xpos][ypos]==0:             #보드 변경 해주기
            aiboard[xpos][ypos]=1
        else:
            aiboard[xpos][ypos]=myboard[xpos][ypos]
    
    elif findboat==2:                           #2번 보트 찾았을때
        xpos=findpos(aiboard,2,1)/10
        ypos=findpos(aiboard,2,1)*10
        aiboard[xpos][ypos]=myboard[xpos][ypos]
    
    elif findboat==3:
        xpos=findpos(aiboard,2,boat3)/10
        ypos=findpos(aiboard,2,boat3)*10
        aiboard[xpos][ypos]=myboard[xpos][ypos]
    else:
        xpos=findpos(aiboard,2,boat4)/10
        ypos=findpos(aiboard,2,boat4)*10
        aiboard[xpos][ypos]=myboard[xpos][ypos]