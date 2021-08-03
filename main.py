<<<<<<< HEAD
a=1
print("김우진 ㅎㅇ")
print("")
=======
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
>>>>>>> a3ac3ffd63d377bd5b396b019c7c82a29c50fe89
