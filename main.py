import ai
import enemyboard


import random
from tkinter import*

window=Tk()

window.title("Battleship by 머저리")
window.geometry("1000x600+100+100")
window.resizable(False, False)
'''
mb=Label(window, text="myboard", bg="yellow", fg="black")
mb.place(x=200, y=10)
eb=Label(window, text="enemyboard", bg="blue", fg="white")
eb.place(x=700, y=10)
'''


for i in range(10):
    for j in range(10):
        test = Label(window, text = enemyboard.Enemyboard.enemy_board[i][j], width = 4, height = 2, relief="solid", bg = "lavender")
        test.grid(row = i, column=j)




window.mainloop()
