ship1='oo'
ship2='ooo'
ship3='oooo'
ship_list={'ship1','ship2','ship3'}



first_ship=input('choose a ship ')
line_one=input('put your first ship\'s line coordinate>')
row_one=input('put your first ship\'s row coordinate>')


ship_list.remove(first_ship)
print(ship_list)
second_ship=input('choose a ship')

line_two=input('put your second ship\'s line coordinate>')
row_two=input('put your second ship\'s row cooredinate>')

ship_list.remove(second_ship)
print(ship_list)
third_ship=input('choose a ship')

line_three=input('put your third ship\'s line coordinates >')
row_three=input('put your third ship\'s line coordinate>')
