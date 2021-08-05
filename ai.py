#ai 부분
import random

class aimove:
                                                                                #따로 보드하나 만듬
    mshowboard= [[0 for col in range(10)] for row in range(10)]
    boat2=0
    boat3=0
    boat4=0

    def initboat(self):                                                       #보트수 초기화
        self.boat2=0
        self.boat3=0
        self.boat4=0

    def findboat(self):                                                       #일단 발견 보트 개수 파악      
        for i in self.mshowboard:
            for j in range(10):
                if self.mshowboardmshowboard[i][j]==2:
                    self.boat2+=1
                elif self.mshowboard[i][j]==3:
                    self.boat3+=1
                elif self.mshowboard[i][j]==4:
                    self.boat4+=1

    def findaddboat(self):                                                    #어떤 보트 추가하는건지 확인           
        if self.boat2==0 and self.boat3==0 and self.boat4==0:                 #랜덤으로 추가해야됨
            return 1
        elif self.boat2==1:                                                   #2번배
            return 2
        elif self.boat3<3 and self.boat3>0:
            return 3
        elif self.boat4<4:
            return 4
        else:
            return 0

    def movevalid(xpos,ypos,self):                                            #입력하려는 점 확인하는 함수
        if xpos>=0 and xpos <=9 and ypos>=0 and ypos<=9 and self.mshowboard[xpos][ypos]==0:
            return True
        else :
            return False

    def findpos(self,findaddboat):                                            #배치 확인  
        boat=findaddboat                                                       #
        if findaddboat==2:
            boatnum=self.boat2
        if findaddboat==3:
            boatnum=self.boat3
        if findaddboat==4:
            boatnum=self.boat4

        if boatnum==1:       
            for i in self.mshowboard:
                for j in i:
                    if self.mshowboard[i][j]==findaddboat:
                        if self.movevalid(i,j+1,self)==True:
                            return i*10+j
                        elif self.movevalid(i+1,j,self)==True:
                            return i*10+j
                        elif self.movevalid(i,j-1,self)==True:
                            return i*10+j
                        elif self.movevalid(i-1,j,self)==True:
                            return i*10+j
        elif boatnum==2:
            a=0
            temp=[0,0,0,0]
            for i in self.mshowboard:
                for j in i:
                    if self.mshowboard[i][j]==findaddboat:
                        a+=1
                        if a==1:
                            temp[0]=i
                            temp[1]=j
                        if a==2:
                            temp[2]=i
                            temp[3]=j
                            break
            if temp[0]==temp[2]:
                if self.movevalid(temp[0],temp[1]-1,self)==True:
                    return temp[0]*10+temp[1]-1
                else:
                    return temp[0]*10+temp[1]+2
            else:
                if self.movevalid(temp[0]-1,temp[1],self)==True:
                    return 10*(temp[0]-1)+temp[1]
                else :
                    return 10*(temp[0]+2)+temp[1]

        else:
            a=0
            temp=[0,0,0,0]
            for i in self.mshowboard:
                for j in i:
                    if self.mshowboardboard[i][j]==findaddboat:
                        a+=1
                        if a==1:
                            temp[0]=i
                            temp[1]=j
                        if a==2:
                            temp[2]=i
                            temp[3]=j
                            break
            if temp[0]==temp[2]:
                if self.movevalid(temp[0],temp[1]-1,self)==True:
                    return temp[0]*10+temp[1]-1
                else:
                    return temp[0]*10+temp[1]+3
            else:
                if self.movevalid(temp[0]-1,temp[1],self)==True:
                    return 10*(temp[0]-1)+temp[1]
                else :
                    return 10*(temp[0]+3)+temp[1]

    def aimove(myboard,self):
        if self.findaddboat==1:                          #보트 찾은 거 없을때 111111111111
            xpos=random.randrange(0,10)
            ypos=random.randrange(0,10)
            while(self.mshowboard[xpos][ypos]!=0):         #쏘는 좌표 정하기
                xpos=random.randrange(0,10)
                ypos=random.randrange(0,10)

            if myboard[xpos][ypos]==0:             #보드 변경 해주기
                self.mshowboard[xpos][ypos]=1
            else:
                self.mshowboard[xpos][ypos]=myboard[xpos][ypos]
        
        elif self.findaddboat==2:                           #2번 보트 찾았을때
            xpos=self.findpos(self,2)/10
            ypos=self.findpos(self,2)*10
            self.mshowboard[xpos][ypos]=2
        
        elif self.findaddboat==3:                           #3번 보트 찾았을때
            xpos=self.findpos(self,3)/10
            ypos=self.findpos(self,3)*10
            self.mshowboard[xpos][ypos]=3
        else:                                               #4번 보트 찾았을때
            xpos=self.findpos(self,4)/10
            ypos=self.findpos(self,4)*10
            self.mshowboard[xpos][ypos]=4