def direction(ship):  #첫번째 배의 방향을 구하는 함수
    if line==10 and row==10: #오른쪽 맨 위쪽 구석((10,10a)으로 잡음)은 자동으로 세로
        select=int(input('본 좌표는 위쪽이나 오른쪽으로 둘 수 없으니 왼쪽(1)으로 두실건지 아래쪽(2)으로 두실건지 고르세요'))
        if select==1:  #1번을 고르면 왼쪽으로 둔다
            direc=-2-ship
        else:      #2번을 고르면 아래쪽으로 둔다
            direc=-1-ship

        
    else:
        list1={1,2}
        print('would you put the ship horizantally(1) or vertically(2)?') #1번 가로와 2번 세로중에서 고르라고 협박중
        direc=int(input('choose your option by number> ')) #고름
        while direc not in list1: #1 2 중에 안고르시는 분들을 위한 부탁
            direc=int(input('1아니면 2중에서 골라주세요> '))
        if direc==1:   
            if line >= 11-ship:      #가로를 골랐으나 범위 벗어날때 왼쪽 방향으로 배치한다
                print('본 좌표에서 오른쪽으로 둘 수 없으니 왼쪽으로 배치됩니다')
                direc=-2-ship
        else:
            if row >=11-ship: #세로를 골랐으나 범위 벗어날때 아래 방향으로 배치한다
                print('본 좌표에서 위쪽으로 둘 수 없으므로 아래쪽으로 배치됩니다')
                direc=-1-ship
            
    return direc

def direction_two(second_ship,line_two,row_two):
    if line_two==10 and row_two==10: #오른쪽 맨 위쪽 구석((10,10)으로 잡음)은 자동으로 세로
        i=int(input('본 좌표는 위쪽이나 오른쪽으로 둘 수 없으니 왼쪽(1)으로 두실건지 아래쪽(2)으로 두실건지 고르세요'))
        if i==1:
            if (row_two ==row_final and(line_two-second_ship <= line_final))or(row_two == row_final and (line_two-second_ship<=line)) : #왼쪽으로 두니까 배1과 겹칠때
                print('왼쪽으로 두면 첫번째 배와 겹치므로 아래쪽으로 배치합니다')
                direc_two=-1-second_ship
            else: #안겹칠때
                direc_two=-2-second_ship
        elif i==2:
            if (line_two==line and row_two-second_ship <= row_final)or(line_two==line_final and row_two-second_ship <= row_final): #아래쪽으로 두니까 배1과 겹칠때
                print('아래쪽으로 두면 첫번째 배와 겹치게 되어 왼쪽으로 배치합니다')
                direc_two=-2-second_ship
            else: #안겹칠때
                direc_two=-1-second_ship

    else:
        list1={1,2}
        print('would you put the ship horizantally(1) or vertically(2)?') #1번 가로와 2번 세로중에서 고르라고 협박중
        direc_two=int(input('choose your option by number> ')) #고름
        while direc_two not in list1:                                       #1 2 중에 안고르시는 분들을 위한 부탁
            direc_two=int(input('1아니면 2중에서 골라주세요> '))
        if direc_two==1:
            if line_two >=11-second_ship:               #가로를 골랐으나 범위를 벗어날때                                       
                if  (row_two-second_ship >= row and row_two-second_ship <=row_final):   #바로 위에서 왼쪽으로 돌렸는데 배1이랑 쳐 겹치면 좌표를 다시 구함
                    print('선택한 좌표에서는 왼쪽으로 배치해도 첫번쨰 배와 겹쳐서 안되므로 새로운 좌표를 구하세요.')
                    line_two=int(input('put your second ship\'s line coordinate from 1~10>')) #배2의 행
                    while line_two<1 or line_two>10:
                        line_two=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_two=int(input('put your second ship\'s row coordinate from 1~10>'))#배2의 열
                    while row_two<1 or row_two>10:                            
                        row_two=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if line_two>=line or line_two<=line_final: #배2의 시작 좌표가 배1이 놓여진 좌표안에 포함될 때
                        while row_two==row:
                            row_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_two<1 or row_two>10: #그새를 못참고 배2 열좌표 좆같이 둘때
                                row_two=int(input('1에서 10사이에서 골라주세요> '))
                    elif row_two>=row or row_two<=row_final:
                        while line_two==line:
                            line_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_two <1 or line_two>10: #그새를 못참고 배2 횡좌표 좆같이 둘때
                                line_two=int(input('1에서 10사이에서만 골라주세요> '))
                    if second_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        second_ship=1
                    elif second_ship=='ship2':
                        second_ship=2
                    else:
                        second_ship=3
                    direction_two(ship2,line_two,row_two)
                else:
                    direc_two=-2-third_ship

                
                        
            elif line_two < 11-second_ship:     #범위를 초과하지는 않지만               
                if  (((row_two>=row and row_two<=row_final)and (line>=line_two and line<=line_two+second_ship))or (row_two==row)and(row_two+second_ship>=row and row_two+second_ship <= row_final)):   #배1과 겹칠때
                    print('이대로 두면 첫번째 배와 겹치므로 좌표를 새로 설정합니다')
                    line_two=int(input('put your second ship\'s line coordinate from 1~10>')) #배2의 행
                    while line_two<1 or line_two>10:
                        line_two=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_two=int(input('put your second ship\'s row coordinate from 1~10>'))#배2의 열
                    while row_two<1 or row_two>10:                            
                        row_two=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if line_two>=line or line_two<=line_final: #배2의 시작 좌표가 배1이 놓여진 좌표안에 포함될 때
                        while row_two==row:
                            row_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_two<1 or row_two>10: #그새를 못참고 배2 열좌표 좆같이 둘때
                                row_two=int(input('1에서 10사이에서 골라주세요> '))
                    elif row_two>=row or row_two<=row_final:
                        while line_two==line:
                            line_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_two <1 or line_two>10: #그새를 못참고 배2 횡좌표 좆같이 둘때
                                line_two=int(input('1에서 10사이에서만 골라주세요> '))
                    if second_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        second_ship=1
                    elif second_ship=='ship2':
                        second_ship=2
                    else:
                        second_ship=3
                    direction_two(ship2,line_two,row_two)

        else:
            if row_two >=11-second_ship:               #세로를 골랐으나 범위를 벗어날때                                       
                if (line_two-second_ship >= line and line_two-second_ship <=line_final) :   #바로 위에서 아래쪽으로 돌렸는데 배1이랑 쳐 겹치면 좌표를 다시 구함
                    print('선택한 좌표에서는 아래쪽으로 배치해도 첫번쨰 배와 겹쳐서 안되므로 새로운 좌표를 구하세요.')
                    line_two=int(input('put your second ship\'s line coordinate from 1~10>')) #배2의 행
                    while line_two<1 or line_two>10:
                        line_two=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_two=int(input('put your second ship\'s row coordinate from 1~10>'))#배2의 열
                    while row_two<1 or row_two>10:                            
                        row_two=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if line_two>=line or line_two<=line_final: #배2의 시작 좌표가 배1이 놓여진 좌표안에 포함될 때
                        while row_two==row:
                            row_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_two<1 or row_two>10: #그새를 못참고 배2 열좌표 좆같이 둘때
                                row_two=int(input('1에서 10사이에서 골라주세요> '))
                    elif row_two>=row or row_two<=row_final:
                        while line_two==line:
                            line_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_two <1 or line_two>10: #그새를 못참고 배2 횡좌표 좆같이 둘때
                                line_two=int(input('1에서 10사이에서만 골라주세요> '))
                    direction_two(second_ship,line_two,row_two)
                else:
                    direc_two=-1-second_ship
                        
            elif row_two < 11-second_ship:     #범위를 초과하지는 않지만               
                if (line_two==line and row_two-second_ship <= row_final)or(line_two==line_final and row_two-second_ship <= row_final): #아래쪽으로 두니까 배1과 겹칠때
                    print('첫번째배와 겹치므로 새로운 좌표를 구하세요.')
                    line_two=int(input('put your second ship\'s line coordinate from 1~10>')) #배2의 행
                    while line_two<1 or line_two>10:
                        line_two=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_two=int(input('put your second ship\'s row coordinate from 1~10>'))#배2의 열
                    while row_two<1 or row_two>10:                            
                        row_two=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if line_two>=line or line_two<=line_final: #배2의 시작 좌표가 배1이 놓여진 좌표안에 포함될 때
                        while row_two==row:
                            row_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_two<1 or row_two>10: #그새를 못참고 배2 열좌표 좆같이 둘때
                                row_two=int(input('1에서 10사이에서 골라주세요> '))
                    elif row_two>=row or row_two<=row_final:
                        while line_two==line:
                            line_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_two <1 or line_two>10: #그새를 못참고 배2 횡좌표 좆같이 둘때
                                line_two=int(input('1에서 10사이에서만 골라주세요> '))
                    if second_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        second_ship=1
                    elif second_ship=='ship2':
                        second_ship=2
                    else:
                        second_ship=3
                    
                    direction_two(second_ship,line_two,row_two)
                    
                
    return direc_two

def direction_three(third_ship,line_third,row_third):
    if line_third==10 and row_third==10:
        i=int(input('본 좌표는 위쪽이나 오른쪽으로 둘 수 없으니 왼쪽(1)으로 두실건지 아래쪽(2)으로 두실건지 고르세요'))
        if i==1:
            if (row_third ==row_final and(line_third-third_ship <= line_final))or(row_third == row_final and (line_third-third_ship<=line)) : #왼쪽으로 두니까 배1과 겹칠때
                print('첫번째 배와 겹치므로 아래쪽으로 배치합니다')
                if (row_third ==row_final and(line_third-third_ship <= line_final))or(row_third == row_final and (line_third-third_ship<=line)) :
                    print('아래쪽으로 둬도 두번째 배와도 겹치므로 새로운 좌표를 설정해야합니다')
                    line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
                    while line_third<1 or line_third>10:
                        line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
                    while row_third<1 or row_third>10:                            
                        row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
                        while row_third==row:
                            row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
                                row_third=int(input('1에서 10사이에서 골라주세요> '))
                        if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
                            row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
                    elif row_third>=row and row_third<=row_final:
                        while line_third==line:
                            line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
                                line_third=int(input('1에서 10사이에서만 골라주세요> '))
                        if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
                            line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

                    if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        third_ship=1
                    elif third_ship=='ship2':
                        third_ship=2
                    else:
                        third_ship=3

                    direc_three=direction_three(third_ship,line_third,row_third)
                    
                else:
                    print('왼쪽으로 두면 첫번째 배와 겹치므로 아래쪽으로 배치합니다')
                    direc_three=-1-third_ship
            else: #안겹칠때
                direc_three=-2-third_ship
        elif i==2:
            if (line_third==line and row_third-third_ship <= row_final)or(line_third==line_final and row_third-third_ship <= row_final): #아래쪽으로 두니까 배1과 겹칠때
                print('아래쪽으로 두면 첫번째 배와 겹치므로 왼쪽으로 배치합니다')
                if (line_third==line_two and row_third-third_ship <= row_final_two)or(line_third==line_final_two and row_third-third_ship <= row_final_two): #아래쪽으로 두니까 배2과 겹칠때
                    print('왼쪽으로 두어도 두번째 배와 겹치므로 새로운 좌표를 설정해야합니다')
                    line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
                    while line_third<1 or line_third>10:
                        line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
                    while row_third<1 or row_third>10:                            
                        row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
                        while row_third==row:
                            row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
                                row_third=int(input('1에서 10사이에서 골라주세요> '))
                        if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
                            row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
                    elif row_third>=row and row_third<=row_final:
                        while line_third==line:
                            line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
                                line_third=int(input('1에서 10사이에서만 골라주세요> '))
                        if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
                            line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

                    if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        third_ship=1
                    elif third_ship=='ship2':
                        third_ship=2
                    else:
                        third_ship=3

                    direc_three=direction_three(third_ship,line_third,row_third)
                else:
                    print('아래쪽으로 두면 첫번째 배와 겹치게 되어 왼쪽으로 배치합니다')
                    direc_third=-2-third_ship
            else: #안겹칠때
                direc_third=-1-third_ship

    else:
        list1={1,2}
        print('would you put the ship horizantally(1) or vertically(2)?') #1번 가로와 2번 세로중에서 고르라고 협박중
        direc_three=int(input('choose your option by number> ')) #고름
        while direc_three not in list1:                                       #1 2 중에 안고르시는 분들을 위한 부탁
            direc_three=int(input('1아니면 2중에서 골라주세요> '))     
        if direc_three==1:
            if line_third >=11-third_ship:               #가로를 골랐으나 범위를 벗어날때                                       
                if  ((row_third-third_ship >= row and row_third-third_ship <=row_final)) or  ((row_third-third_ship >= row_two and row_third-third_ship <=row_final_two)): #왼쪽으로 돌렸으나 배1이나 배2를 만날때
                    print('왼쪽으로 배치해도 배1또는 배2와 겹치므로 좌표를 새로 설정합니다')
                    line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
                    while line_third<1 or line_third>10:
                        line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
                    while row_third<1 or row_third>10:                            
                        row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
                        while row_third==row:
                            row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
                                row_third=int(input('1에서 10사이에서 골라주세요> '))
                        if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
                            row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
                    elif row_third>=row and row_third<=row_final:
                        while line_third==line:
                            line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
                                line_third=int(input('1에서 10사이에서만 골라주세요> '))
                        if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
                            line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

                    if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        third_ship=1
                    elif third_ship=='ship2':
                        third_ship=2
                    else:
                        third_ship=3
                
                    direc_three=direction_three(third_ship,line_third,row_third)
                else:
                    direc_three=-2-third_ship

            elif line_third < 11-third_ship:     #범위를 초과하지는 않지만               
                if((((row_third>=row and row_third<=row_final)and (line>=line_third and line<=line_third+third_ship))or (row_third==row)and(row_third+third_ship>=row and row_third+third_ship <= row_final))) and (((row_third>=row_two and row_third<=row_final_two)and (line_two>=line_third and line_two<=line_third+third_ship))or (row_third==row_two)and(row_third+third_ship>=row_two and row_third+third_ship <= row_final_two)): #배1과 배2모두 겹칠때
                    print('첫번째 배와 두번째 배와 겹치므로 새로운 좌표를 정합니다')
                    line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
                    while line_third<1 or line_third>10:
                        line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
                    while row_third<1 or row_third>10:                            
                        row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
                        while row_third==row:
                            row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
                                row_third=int(input('1에서 10사이에서 골라주세요> '))
                        if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
                            row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
                    elif row_third>=row and row_third<=row_final:
                        while line_third==line:
                            line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
                                line_third=int(input('1에서 10사이에서만 골라주세요> '))
                        if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
                            line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

                    if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        third_ship=1
                    elif third_ship=='ship2':
                        third_ship=2
                    else:
                        third_ship=3

                    direc_three=direction_three(third_ship,line_third,row_third)
                
        else:
            if row_third >=11-third_ship:          #세로를 골랐으나 범위를 벗어날때  
                if (((line_third-third_ship >= line and line_third-third_ship <=line_final)) or((line_third-third_ship >= line_two and line_third-third_ship <=line_final_two))): #아래로 하니까 배1이나 배2를 만났을때
                    print('아래쪽으로 배치하면 첫번째 배 아니면 두번째 배를 만나므로 좌표를 새로 정합니다.')
                    line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
                    while line_third<1 or line_third>10:
                        line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
                    while row_third<1 or row_third>10:                            
                        row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
                        while row_third==row:
                            row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
                                row_third=int(input('1에서 10사이에서 골라주세요> '))
                        if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
                            row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
                    elif row_third>=row and row_third<=row_final:
                        while line_third==line:
                            line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
                                line_third=int(input('1에서 10사이에서만 골라주세요> '))
                        if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
                            line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

                    if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        third_ship=1
                    elif third_ship=='ship2':
                        third_ship=2
                    else:
                        third_ship=3

                    direc_three=direction_three(third_ship,line_third,row_third)
                else:
                    direc_three=-1-third_ship

            elif row_third <11-third_ship: #범위는 벗어나지 않지만
                if (((line_third-third_ship >= line and line_third-third_ship <=line_final)) or((line_third-third_ship >= line_two and line_third-third_ship <=line_final_two))): #아래로 하니까 배1이나 배2를 만났을때:
                    print('첫번째 배 또는 두번째 배와 만나므로 좌표를 새로 설정합니다')
                    line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
                    while line_third<1 or line_third>10:
                        line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
                    row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
                    while row_third<1 or row_third>10:                            
                        row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

                    if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
                        while row_third==row:
                            row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
                            while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
                                row_third=int(input('1에서 10사이에서 골라주세요> '))
                        if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
                            row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
                    elif row_third>=row and row_third<=row_final:
                        while line_third==line:
                            line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
                            while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
                                line_third=int(input('1에서 10사이에서만 골라주세요> '))
                        if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
                            line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

                    if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
                        third_ship=1
                    elif third_ship=='ship2':
                        third_ship=2
                    else:
                        third_ship=3

                    direc_three=direction_three(third_ship,line_third,row_third)
    return direc_three

                
        



ship1=2
ship2=3
ship3=4
ship_list={'ship1','ship2','ship3'}


print(ship_list)   #배의 리스트 먼저 보여줌
print('ship1\'s size is 2, ship2\'s size is 3 , ship3\'s size is 4') #배 크기 알려줌
ship=input('choose a ship inside the list> ') #배 먼저 선택 줄여서 배선이라고함

while ship not in ship_list:  #좆같이 고르면 다시 고르라함 줄여서 배좆고라고함
    ship=(input('choose a correct ship inside the list> '))

ship_list.remove(ship) #고른배는 위의 리스트에서 제거 

line=int(input('put your first ship\'s line coordinate from 1~10>')) #배1의 행
while line<1 or line>10:
    line=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
row=int(input('put your first ship\'s row coordinate from 1~10>'))#배1의 열
while row<1 or row>10:                            
    row=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

if ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
    ship=1
elif ship=='ship2':
    ship=2
else:
    ship=3

direc=direction(ship)



if direc==1:       #가로면 가로의 끝좌표 구하기
    line_final=line+ship
    row_final=row
elif direc==2:      #세로면 세로의 끝좌표 구하기
    row_final=row+ship
    line_final=line
elif direc==-1-ship:            #최종적으로 아래쪽으로 두었을때
    row=row-ship
    row_final=row
    line_final=line
else:                           #최종적으로 왼쪽으로 두었을떄 
    row_final=row
    line=line-ship
    line_final=line

    

print(line_final)    #그냥 가로 세로의 끝 좌표가 제대로 구해졌는지 확인용
print(row_final)

       
print(ship_list)    #남은 배의 목록 보여주기

second_ship=input('choose a ship inside the list> ') #배2선택

while second_ship not in ship_list:  #배좆고2
    second_ship=(input('choose a correct ship inside the list> '))

ship_list.remove(second_ship)  #고른배 리스트에서 제거

line_two=int(input('put your second ship\'s line coordinate from 1~10>')) #배2의 행
while line_two<1 or line_two>10:
    line_two=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
row_two=int(input('put your second ship\'s row coordinate from 1~10>'))#배2의 열
while row_two<1 or row_two>10:                            
    row_two=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

if line_two>=line and line_two<=line_final: #배2의 시작 좌표가 배1이 놓여진 좌표안에 포함될 때
    while row_two==row:
        row_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
        while row_two<1 or row_two>10: #그새를 못참고 배2 열좌표 좆같이 둘때
            row_two=int(input('1에서 10사이에서 골라주세요> '))
elif row_two>=row and row_two<=row_final:
    while line_two==line:
        line_two=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
        while line_two <1 or line_two>10: #그새를 못참고 배2 횡좌표 좆같이 둘때
            line_two=int(input('1에서 10사이에서만 골라주세요> '))


if second_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
    second_ship=1
elif second_ship=='ship2':
    second_ship=2
else:
    second_ship=3

direc_two=direction_two(second_ship,line_two,row_two)  #방향 구하기




if direc_two==1:       #가로면 가로의 끝좌표 구하기
    line_final_two=line_two+second_ship
    row_final_two=row_two
elif direc_two==2:      #세로면 세로의 끝좌표 구하기
    row_final_two=row_two+second_ship
    line_final_two=line_two
elif direc_two==-1-second_ship:            #최종적으로 아래쪽으로 두었을때
    row_two=row_two-second_ship
    row_final_two=row_two
    line_final_two=line_two
else:                          #최종적으로 왼쪽으로 두었을떄 
    row_final_two=row_two
    line_two=line_two-second_ship
    line_final_two=line_two

    #dd

print(line_final_two)    #그냥 가로 세로의 끝 좌표가 제대로 구해졌는지 확인용
print(row_final_two)
print(line_two)
print(row_two)


print(ship_list)  #남은 배 목록
third_ship=input('choose a ship') #배선3
while third_ship not in ship_list: #배좆고3
    third_ship=input('리스트안의 배를 고르시오')

line_third=int(input('put your third ship\'s line coordinate from 1~10>')) #배3의 행
while line_third<1 or line_third>10:
    line_third=int(input('1에서 10사이에서만 골라주세요> ')) #공손하게 부탁1
row_third=int(input('put your third ship\'s row coordinate from 1~10>'))#배3의 열
while row_third<1 or row_third>10:                            
    row_third=int(input('1에서 10사이에서만 골라주세요> '))   #공손하게 부탁2

if (line_third>=line and line_third<=line_final): #배3의 시작 좌표가 배1 또는 배2가 놓여진 좌표안에 포함될 때
    while row_third==row:
        row_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 열 좌표를 다시 골라주세요> '))
        while row_third<1 or row_third>10: #그새를 못참고 배3 열좌표 좆같이 둘때
            row_third=int(input('1에서 10사이에서 골라주세요> '))
    if ((line_third>=line_two and line_third<=line_final_two))and (row_third==row_two):
        row_third=int(input('시작 좌표가 두번째 배와 겹칩니다 배의 열 좌표를 다시 골라주세요'))
elif row_third>=row and row_third<=row_final:
    while line_third==line:
        line_third=int(input('첫번째 배와 시작 좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요> '))
        while line_third <1 or line_third>10: #그새를 못참고 배3 횡좌표 좆같이 둘때
            line_third=int(input('1에서 10사이에서만 골라주세요> '))
    if ((row_third>=row_two and row_third<=row_final_two))and(line_third==line_two):
        line_third=int(input('첫번째 배와 시작좌표가 겹칩니다 배의 행 좌표를 다시 골라주세요'))

if third_ship=='ship1':  #고른배를 정수로 바꿔서 위에 함수에 대입
    third_ship=1
elif third_ship=='ship2':
    third_ship=2
else:
    third_ship=3

direc_three=direction_three(third_ship,line_third,row_third)

if direc_three==1:       #가로면 가로의 끝좌표 구하기
    line_final_three=line_third+third_ship
    row_final_three=row_third
elif direc_three==2:      #세로면 세로의 끝좌표 구하기
    row_final_three=row_third+third_ship
    line_final_three=line_third
elif direc_three==-1-third_ship:            #최종적으로 아래쪽으로 두었을때
    row_third=row_third-third_ship
    row_final_three=row_third
    line_final_three=line_third
else:                          #최종적으로 왼쪽으로 두었을떄 
    row_final_three=row_third
    line_third=line_third-third_ship
    line_final_three=line_third

    

print(line_final_three)    #그냥 가로 세로의 끝 좌표가 제대로 구해졌는지 확인용
print(row_final_three)
print(line_third)
print(row_third)
