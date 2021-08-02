#ai 부분


class Aiboard:
    def initboard():                                                           #따로 보드하나 만듬
        aiboard= [[0 for col in range(10)] for row in range(10)]

    def initnumboat():                                                         #격추시킨 수 초기화
        boat2=0
        boat3=0
        boat4=0

    def findboat(board,boat2,boat3,boat4):                                     #일단 보트를 찾아야 됨
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

