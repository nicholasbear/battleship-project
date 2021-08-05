my_board = [[0 for col in range(10)] for row in range(10)]
ship_list=['ship1','ship2','ship3']
count = 0

while count < 3:
    print(ship_list)   #배의 리스트 먼저 보여줌
    print('ship1\'s size is 2, ship2\'s size is 3 , ship3\'s size is 4') #배 크기 알려줌
    ship=input('리스트 안의 배 중 하나를 고르세요')
    if ship not in ship_list:
        continue
    ship_list.remove(ship) #고른배는 위의 리스트에서 제거

    if ship == 'ship1':
        shipsize = 2
    if ship == 'ship2':
        shipsize = 3
    if ship == 'ship3':
        shipsize = 4

    print("놓을 배의 시작부분의 x좌표와 y좌표를 적으세요")
    while True:
        print("10 이내의 자연수 중에서 고르세요")
        col = int(input("x :"))       #x좌표는 colon
        if col <= 11-shipsize and col > 0:
            col -= 1
            break
        print("배의 크기",shipsize,"를 생각해서 좌표를 정해주세요")
    while True:
        print("10 이내의 자연수 중에서 고르세요")
        row = 11 - int(input("y :"))  #y좌표는 11-row
        if row <= 10 and row >= shipsize:
            row -= 1
            break
        print("배의 크기",shipsize,"를 생각해서 좌표를 정해주세요")
    while True:
        print("가로 : 1, 세로 : 2 // 1,2중 하나를 고르세요")
        dir = int(input("가로/세로 : "))
        if dir < 3 and dir > 0:
            break

    sum = 0
    if dir == 1: #배가 가로로 놓임
        for i in range (shipsize):
            sum += my_board[row][col+i]
        if sum == 0:
            for i in range (shipsize):
                my_board[row][col+i] = shipsize
        else:
            print("기존의 배와 겹칩니다. 다시 입력해주세요")
            ship_list.append(ship)
            continue

    if dir == 2: #배가 세로로 놓임
        for i in range (shipsize):
            sum += my_board[row-i][col]
        if sum == 0:
            for i in range (shipsize):
                my_board[row-i][col] = shipsize
        else:
            print("기존의 배와 겹칩니다. 다시 입력해주세요")
            ship_list.append(ship)
            continue

    for i in range(10):
        print(my_board[i])

    count += 1