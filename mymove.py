﻿import tkinter.messagebox as msgbox
from tkinter import *
import enemyboard

def targetHit(): #배를 맞췄을때
        xpos = int(input("x좌표를 입력하세요: "))
        ypos = int(input("y좌표를 입력하세요: "))
        boat2 = 2
        boat3 = 3
        boat4 = 4
        root = Tk()
        root.withdraw()       

        if enemyboard.Enemyboard.enemy_board[xpos][ypos] == 2:
           boat2 -= 1
           enemyboard.Enemyboard.enemy_board[xpos][ypos] = 1 #배가 맞으면 표시
           msgbox.showinfo("성공", "배를 성공적으로 맞췄습니다!")
        elif enemyboard.Enemyboard.enemy_board[xpos][ypos] == 3:
             boat3 -= 1
             enemyboard.Enemyboard.enemy_board[xpos][ypos] = 1 
             msgbox.showinfo("성공", "배를 성공적으로 맞췄습니다!")
        elif enemyboard.Enemyboard.enemy_board[xpos][ypos] == 4:
             boat4 -= 1
             enemyboard.Enemyboard.enemy_board[xpos][ypos] = 1 
             msgbox.showinfo("성공", "배를 성공적으로 맞췄습니다!")
        if boat2 == 0:
           root = Tk()
           root.withdraw()
           msgbox.showinfo("격추", "1번배를 성공적으로 격추시켰습니다!")
        if boat3 == 0:
           root = Tk()
           root.withdraw()
           msgbox.showinfo("격추", "2번배를 성공적으로 격추시켰습니다!")
        if boat4 == 0:
           root = Tk()
           root.withdraw()
           msgbox.showinfo("격추", "3번배를 성공적으로 격추시켰습니다!")
            
def targetMiss(): #배를 못맞췄을때
        xpos = int(input("x좌표를 입력하세요: "))
        ypos = int(input("y좌표를 입력하세요: "))
        root = Tk()
        root.withdraw()
        if enemyboard.Enemyboard.enemy_board[xpos][ypos] == 0:
           msgbox.showerror("실패", "배를 맞추지 못했습니다!")
        elif enemyboard.Enemyboard.enemy_board[xpos][ypos] == 1:
           msgbox.showerror("실패", "이미 맞춘 부분입니다.")
targetHit()
targetMiss()





