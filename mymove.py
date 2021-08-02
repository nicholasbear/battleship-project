import tkinter.messagebox as msgbox
from tkinter import *

def targetHit(): #배를 맞췄을때
    root = Tk()
    root.withdraw()
    msgbox.showinfo("성공", "배를 성공적으로 맞췄습니다!")
def targetMiss(): #배를 못맞췄을때
    root = Tk()
    root.withdraw()
    msgbox.showerror("실패", "배를 맞추지 못했습니다!")
def boat2Clear(): #1번배 격추
    root = Tk()
    root.withdraw()
    msgbox.showinfo("격추", "1번배를 성공적으로 격추시켰습니다!")
def boat3Clear(): #2번배 격추
    root = Tk()
    root.withdraw()
    msgbox.showinfo("격추", "2번배를 성공적으로 격추시켰습니다!")
def boat4Clear(): #3번배 격추
    root = Tk()
    root.withdraw()
    msgbox.showinfo("격추", "3번배를 성공적으로 격추시켰습니다!")
targetHit()
targetMiss()
boat2Clear()
boat3Clear()
boat4Clear()



