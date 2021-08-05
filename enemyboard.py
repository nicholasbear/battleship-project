# baebaebuae
import random as rd

class Enemyboard:
    enemy_board = [[0 for col in range(10)] for row in range(10)]

    def printboard(self): #랜덤으로 잘 놓여졌는지 확인하는 용도
        for i in range(10):
            print(self.enemy_board[i])

    def clear(self): #초기화 Hoxy몰라서 만들어둠
        self.enemy_board = [[0 for col in range(10)] for row in range(10)]

    def get_ship(self,shipsize):
        a = rd.randint(0,10-shipsize)
        b = rd.randint(0,10-shipsize)
        c = rd.randint(0,1)
        sum = 0

        if c == 0: #배가 가로로 놓임
            for i in range (shipsize):
                sum += self.enemy_board[a][b+i]
            if sum == 0:
                for i in range (shipsize):
                    self.enemy_board[a][b+i] = shipsize
            else:
                self.get_ship(shipsize)
        
        if c == 1: #배가 세로로 놓임
            for i in range (shipsize):
                sum += self.enemy_board[a+i][b]
            if sum == 0:
                for i in range (shipsize):
                    self.enemy_board[a+i][b] = shipsize
            else:
                self.get_ship(shipsize)

