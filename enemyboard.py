# baebaebuae
import random as rd

class Enemyboard:
    enemy_board = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

    a=0
    b=0
    c=0

    def printboard(self):
        for i in range(0,9):
            print(self.enemy_board[i])

    def clear(self):
        self.enemy_board = [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

    def get_largeship(self):
        a = rd.randint(0,6)
        b = rd.randint(0,6)
        c = rd.randint(0,1)
        sum = 0

        if c == 0: #배가 가로로 놓임
            for i in range (4):
                sum += self.enemy_board[a][b+i]
                if sum == 0:
                    self.enemy_board[a][b+i] = 4
                else:
                    self.get_largeship()
        
        if c == 1: #배가 세로로 놓임
            for i in range (4):
                sum += self.enemy_board[a+i][b]
                if sum == 0:
                    self.enemy_board[a+i][b] = 4
                else:
                    self.get_largeship()
    
    def get_mediumship(self):
        a = rd.randint(0,7)
        b = rd.randint(0,7)
        c = rd.randint(0,1)
        sum = 0

        if c == 0: #배가 가로로 놓임
            for i in range (3):
                sum += self.enemy_board[a][b+i]
                if sum == 0:
                    self.enemy_board[a][b+i] = 3
                else:
                    self.get_mediumship()
        
        if c == 1: #배가 세로로 놓임
            for i in range (3):
                sum += self.enemy_board[a+i][b]
                if sum == 0:
                    self.enemy_board[a+i][b] = 3
                else:
                    self.get_mediumship()

    def get_smallship(self):
        a = rd.randint(0,8)
        b = rd.randint(0,8)
        c = rd.randint(0,1)
        sum = 0

        if c == 0: #배가 가로로 놓임
            for i in range (2):
                sum += self.enemy_board[a][b+i]
                if sum == 0:
                    self.enemy_board[a][b+i] = 2
                else:
                    self.get_smallship()
        
        if c == 1: #배가 세로로 놓임
            for i in range (2):
                sum += self.enemy_board[a+i][b]
                if sum == 0:
                    self.enemy_board[a+i][b] = 2
                else:
                    self.get_smallship()
    
    def start(self):
        enemyboard.clear()
        enemyboard.get_largeship()
        enemyboard.get_mediumship()
        enemyboard.get_smallship()

enemyboard = Enemyboard()
enemyboard.start()
enemyboard.printboard()