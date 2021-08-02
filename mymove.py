import tkinter.messagebox as msgbox
from tkinter import *

def targetHit():
    root = Tk()
    root.withdraw()
    msgbox.showinfo("성공", "배를 성공적으로 맞췄습니다!")
def targetMiss():
    root = Tk()
    root.withdraw()
    msgbox.showerror("실패", "배를 맞추지 못했습니다!")

def targetClear():
    root = Tk()
    root.withdraw()
    msgbox.showinfo("격추", "배를 성공적으로 격추시켰습니다!")
targetHit()
targetMiss()
targetClear()


