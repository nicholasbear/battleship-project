import random as rd
from tkinter import*
from tkinter import font
from copy import deepcopy

game1 = [["", "", 5, 3, "", "", "", "", ""],
        [8, "", "", "", "", "", "", 2, ""],
        ["", 7, "", "", 1, "", 5, "", ""],
        [4, "", "", "", "", 5, 3, "", ""],
        ["", 1, "", "", 7, "", "", "", 6],
        ["", "", 3, 2, "", "", "", 8, ""],
        ["", 6, "", 5, "", "", "", "", 9],
        ["", "", 4, "", "", "", "", 3, ""],
        ["", "", "", "", "", 9, 7, "", ""]]
game1_answer=[[1,4,5,3,2,7,6,9,8],
             [8,3,9,6,5,4,1,2,7],
             [6,7,2,9,1,8,5,4,3],
             [4,0,6,1,8,5,3,7,2],
             [2,1,8,4,7,3,9,5,6],
             [7,5,3,2,9,6,4,8,1],
             [3,6,7,5,4,2,8,1,9],
             [9,8,4,7,6,1,2,3,5],
             [5,2,1,8,3,9,7,6,4]]
game2=[["",9,"",1,"",6,"","",""],
       ["","",6,"","",2,7,"",""],
       ["",3,2,"","","","","",""],
       ["",1,7,4,5,"","","",3],
       ["","",3,"","","",5,"",""],
       [4,"","","",8,3,9,2,""],
       ["","","","","","",6,5,""],
       ["","",4,2,"","",3,"",""],
       ["","","",3,"",7,"",9,""]]
game2_answer=[[7,9,8,1,4,6,2,3,5],
              [1,4,6,5,3,2,7,8,9],
              [5,3,2,9,7,8,1,4,6],
              [2,1,7,4,5,9,8,6,3],
              [9,8,3,6,2,1,5,7,4],
              [4,6,5,7,8,3,9,2,1],
              [3,2,9,8,1,4,6,5,7],
              [6,7,4,2,9,5,3,1,8],
              [8,5,1,3,6,7,4,9,2]]
game3=[[7,"","","","",9,3,4,8],
       ["","","","",4,"","",1,""],
       ["","","",5,"","","","",""],
       [9,1,"",4,"","","",7,""],
       [6,"","",9,"",3,"","",1],
       ["",3,"","","",1,"",2,9],
       ["","","","","",5,"","",""],
       ["",8,"","",1,"","","",""],
       [4,9,3,8,"","","","",2]]
game3_answer=[[7,5,6,1,2,9,3,4,8],
              [3,2,9,6,4,8,7,1,5],
              [8,4,1,5,3,7,2,9,6],
              [9,1,8,4,6,2,5,7,3],
              [6,7,2,9,5,3,4,8,1],
              [5,3,4,7,8,1,6,2,9],
              [1,6,7,2,9,5,8,3,4],
              [2,8,5,3,1,4,9,6,7],
              [4,9,3,8,7,6,1,5,2]]
game4= [[3, "", "", 9, "", 1, 6, 5, ""],
        [1, 2,"", "", 3, 7, 4, "", 8],
        ["", 7, 5, "", "", 6, "", 3, 1],
        [8, 5, 1, 2, "", 4, "", "", 3],
        ["", 3, 2, 7, 5, 8, 1, 4, 9],
        [4, "", "", 6, "", 3, 8, "", ""],
        [7, 4, "", 3, "", "", 5, 1, ""],
        [2, "", 3, 8, 4, "", "", 7, 6],
        ["", "", 9, 1, "", 2, "", "", 4]]
game4_answer=[[3,8,4,9,2,1,6,5,7],
             [1,2,6,5,3,7,4,9,8],
             [9,7,5,4,8,6,2,3,1],
             [8,5,1,2,9,4,7,6,3],
             [6,3,2,7,5,8,1,4,9],
             [4,9,7,6,1,3,8,2,5],
             [7,4,8,3,6,9,5,1,2],
             [2,1,3,8,4,5,9,7,6],
             [5,6,9,1,7,2,3,8,4]]
game5=[["",4,7,"","","",5,"",1],
       [2,"","",8,"",7,"",6,""],
       [6,"","",1,"",5,"","",4],
       ["",7,9,"","","",2,3,""],
       ["","","","","","","","",""],
       ["",6,8,"",7,"",1,4,""],
       [3,"","",9,"",7,"","",5],
       ["",9,"",2,"",6,"","",8],
       [8,"",1,"","","",6,9,""]]
game5_answer=[[9,4,7,6,2,3,5,8,1],
              [2,1,5,8,4,7,9,6,3],
              [6,8,3,1,9,5,7,2,4],
              [4,7,9,5,1,8,2,3,6],
              [1,3,2,4,6,9,8,5,7],
              [5,6,8,3,7,2,1,4,9],
              [3,2,6,9,8,1,4,7,5],
              [7,9,4,2,5,6,3,1,8],
              [8,5,1,7,3,4,6,9,2]]
game6=[["","",3,7,"",4,5,"",""],
       ["",2,"","","","","",6,""],
       ["",8,"",3,1,6,"",2,""],
       ["","","","","","","","",""],
       [3,7,"","","","","",9,2],
       [2,"",4,"","","",8,"",6],
       ["",4,"",1,3,5,"",7,""],
       ["",5,"","","","","",4,""],
       ["","",1,6,"",7,2,"",""]]
game6_answer=[[6,9,3,7,2,4,5,1,8],
              [1,2,7,8,5,9,3,6,4],
              [4,8,5,3,1,6,9,2,7],
              [5,6,9,4,8,2,7,3,1],
              [3,7,8,5,6,1,4,9,2],
              [2,1,4,9,7,3,8,5,6],
              [8,4,2,1,3,5,6,7,9],
              [7,5,6,2,9,8,1,4,3],
              [9,3,1,6,4,7,2,8,5]]

arr=[[[]for i in range(9)]for i in range(9)]


def sudoku(sudoku_list,a_list_answer):
    a_list = deepcopy(sudoku_list)  ## 스도쿠 원본 리스트를 a_list라는 리스트를 만들어 복사해줌
    
    ## test_row, test_col, test_square는 num_input이라는 함수에 사용되는 함수
    def test_row(row,count,a_list,x):  ## test_row는 가로줄이 틀렸는지 확인하는 함수
        row_list = []                  
        row_list = a_list[row][:]  ## 입력한 행 전체를 row_list에 복사함
        
        for i in range(row_list.count("")):  ## row_list에 있는 ""를 삭제 -> row_list에는 숫자만 남아있음
            row_list.remove("")

        if len(row_list) != len(set(row_list)):  ## row_list의 길이와 row_list에서 중복된 숫자들을 제거한 길이를 비교
            count = 1                            ## 둘의 길이가 다를 경우 스도쿠의 가로줄에 중복된 숫자가 있다는 뜻
            x = 1
            for i in range(9):  ## 둘의 길이가 다를 경우 가로줄에 붉은 색을 칠함
                arr[row][i].config(fg = "red")
        else:
            for i in range(9):  ## 둘의 길이가 같을 경우 가로줄을 다시 검은색으로 칠함
                arr[row][i].config(fg = "black")

        return count,x

    def test_col(col,count,a_list,y):  ## 세로줄이 틑렸는지 확인하는 test_row와 같은 원리의 함수, 위의 주석을 참고바람
        col_list = []  
        
        for i in range(9):  ## col_list에 세로줄을 입력
            col_list.append(a_list[i][col])

        for i in range(col_list.count("")):
            col_list.remove("")   

        if len(col_list) != len(set(col_list)):
            count = 1
            y = 1
            for i in range(9):
                arr[i][col].config(fg = "red")
        else:
            for i in range(9):
                arr[i][col].config(fg = "black")

        return count,y

    def test_square(row,col,count,a_list,z):  ## 네모칸이 틑렸는지 확인하는 test_row와 같은 원리의 함수, 위의 주석을 참고바람
        square_list = []
        
        for i in range(3):  ## square_list에 네모칸을 입력
            for j in range(3):
                square_list.append(a_list[i+row*3][j+col*3])

        for i in range(square_list.count("")):
            square_list.remove("")

        if len(square_list) != len(set(square_list)):
            count = 1
            z = 1
            for i in range(3):
                for j in range(3):
                    arr[i+row*3][j+col*3].config(fg = "red")
        else:
            for i in range(3):
                for j in range(3):
                    arr[i+row*3][j+col*3].config(fg = "black")

        return count,z
    
    def num_input():  ## 숫자 입력 버튼을 누르면 실행되는 함수
        row = int(entry1.get())-1
        col = int(entry2.get())-1
        num = int(entry3.get())
        
        count = 0
        x = 0
        y = 0
        z = 0
        
        arr[row][col].config(text = num, relief = "ridge", bg = "alice blue")  ##입력한 값을 알아볼 수 있게 테두리와 색을 변경
        a_list[row][col] = int(num)  ##a_list에 입력값 대입

        count,x = test_row(row,count,a_list,x)

        count,y = test_col(col,count,a_list,y)

        count,z = test_square(int(row/3),int(col/3),count,a_list,z)

        ## 글씨가 온전히 붉은색으로 변하지 않는 오류 수정 코드
        if ((x == 1) and (y == 0) and (z == 0)):
            count,x = test_row(row,count,a_list,x)   

        elif ((x == 0) and (y == 1) and (z == 0)):
            count,y = test_col(col,count,a_list,y)

        elif ((x == 1) and (y == 1) and (z == 0)):
            count,x = test_row(row,count,a_list,x)
            count,y = test_col(col,count,a_list,y)
            
        ## 붉은색이어야 하는 입력값이 최종적으로 검은색이 되는 오류 수정 코드
        if count == 1:
            arr[row][col].config(fg = "red")
            
    def solve():  ## 정답 확인 버튼을 누르면 실행되는 함수
        if a_list == a_list_answer:
            Label(window, text = "축하합니다! 정답입니다!",width = 40, bg = "ghost white").place(x = 30, y = 230)
        else:
            Label(window, text = "틀렸습니다. 다시 시도하세요.",width = 30, bg = "ghost white").place(x = 30, y = 230)
    
    def clear():  ## 초기화 버튼을 누르면 실행되는 함수
        row_index = 0
        col_index = 0
        for i in range(9):  ## sudoku_list로 스도쿠 판을 다시 만듦
            for j in range(9):
                arr[i][j] = Label(window, text = sudoku_list[i][j], width = 2, height = 1, font = font1, relief="solid", bg = "lavender")
                arr[i][j].grid(row = row_index, column=col_index)
                col_index += 1
                if col_index > 8:
                    row_index += 1
                    col_index = 0
                    
                
    window=Tk()  ## 두번째 스도쿠 풀이 창을 띄우는 시작부분
    window.geometry('480x300')
    window.config(bg = "ghost white")
    
    font1=font.Font(size=15)
    
    row_index = 0
    col_index = 0
    for i in range(9):  ## sudoku_list로 스도쿠 판을 만듦
        for j in range(9):
            arr[i][j] = Label(window, text = sudoku_list[i][j], width = 2, height = 1, font = font1, relief="solid", bg = "lavender")
            arr[i][j].grid(row = row_index, column=col_index)
            col_index += 1
            if col_index > 8:
                row_index += 1
                col_index = 0
    
    label1 = Label(window, text = "행 : ",bg = "ghost white")
    label1.place(x = 260, y = 30)
    entry1 = Entry(window, width = 5)
    entry1.place(x = 290, y = 30)

    label2 = Label(window, text = "열 : ",bg = "ghost white")
    label2.place(x = 370, y = 30)
    entry2 = Entry(window, width = 5)
    entry2.place(x = 400, y = 30)

    label3 = Label(window, text = "숫자 : ",bg = "ghost white")
    label3.place(x = 300, y = 70)
    entry3 = Entry(window, width = 5)
    entry3.place(x = 340, y = 70)    

    button1 = Button(window, text = "숫자 입력", bg = "alice blue", command = num_input)
    button1.place(x = 310, y = 120)
    
    button2 = Button(window, text = "정답 확인", bg = "honeydew", command = solve)
    button2.place(x = 310, y = 160)
    
    button3 = Button(window, text = "초기화", bg = "ivory", command = clear)
    button3.place(x = 310, y = 200)
    
    window.mainloop()  
    
    
def easy():  
    easy=[game1, game4]
    easy_answer = [game1_answer, game4_answer]
    a=rd.randint(0, 1)
    sudoku(easy[a],easy_answer[a])
    
def medium():
    medium=[game2, game5]
    medium_answer = [game2_answer, game5_answer]
    a=rd.randint(0, 1)
    sudoku(medium[a],medium_answer[a])
    
def hard():
    hard=[game3, game6]
    hard_answer=[game3_answer, game6_answer]
    a=rd.randint(0, 1)
    sudoku(hard[a],hard_answer[a])


window=Tk()  ## 첫번째 창을 띄우는 코드의 시작부분
window.geometry('480x300')

font1=font.Font(size=15)

Label(window, text = "난이도를 선택하세요").place(x = 170, y = 100)

button_easy = Button(window, text = "easy", command = easy).place(x = 100, y = 170)
button_medium = Button(window, text = "medium", command = medium).place(x = 210, y = 170)
button_hard = Button(window, text = "hard", command = hard).place(x = 350, y = 170)

window.mainloop()