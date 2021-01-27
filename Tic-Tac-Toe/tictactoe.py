win_list = []


def check_winning():
    # Check each row
    if cells['1 3'] == cells['2 3'] == cells['3 3']:
        win_list.append(cells['1 3'])
    if cells['1 2'] == cells['2 2'] == cells['3 2']:
        win_list.append(cells['1 2'])
    if cells['1 1'] == cells['2 1'] == cells['3 1']:
        win_list.append(cells['1 1'])

    # Check each column
    if cells['1 3'] == cells['1 2'] == cells['1 1']:
        win_list.append(cells['1 3'])
    if cells['2 3'] == cells['2 2'] == cells['2 1']:
        win_list.append(cells['2 3'])
    if cells['3 3'] == cells['3 2'] == cells['3 1']:
        win_list.append(cells['3 3'])

    # Check the X
    if cells['1 3'] == cells['2 2'] == cells['3 1']:
        win_list.append(cells['1 3'])
    if cells['3 3'] == cells['2 2'] == cells['1 1']:
        win_list.append(cells['3 3'])
    return win_list


def result():
    if turns != 9:
        if 'X' in win_list or 'O' in win_list:
            return f'{win_list[-1]} wins'
    else:
        if 'X' in win_list or 'O' in win_list:
            return f'{win_list[-1]} wins'
        else:
            return 'Draw'


cells = {
    '1 3': ' ', '2 3': ' ', '3 3': ' ',
    '1 2': ' ', '2 2': ' ', '3 2': ' ',
    '1 1': ' ', '2 1': ' ', '3 1': ' '
}

print("\nStart with 'X', follow by 'O'")
print('Please enter the coordinate to place your option. The coordinates are listed as below:')
print('''---------
| {'1 3'} {'2 3'} {'3 3'} |
| {'1 2'} {'2 2'} {'3 2'} |
| {'1 1'} {'2 1'} {'3 1'} |
---------
''')

turns = 0

while True:
    coordinate = str()
    while len(coordinate) != 3:
        coordinate = input('Enter the coordinates: ')
        if len(coordinate) < 3:
            print('Please enter 2 numbers seperate with space')


    if coordinate.replace(' ', '').isdecimal() == True:
        coordinate_a, coordinate_b = coordinate.split()
        if 0 < int(coordinate_a) <= 3 and 0 < int(coordinate_b) <= 3:
            if coordinate in cells.keys():
                if cells[coordinate] == ' ' or cells[coordinate] == '_':
                    if turns % 2 == 0:
                        cells[coordinate] = 'X'
                        print('---------')
                        print(f"| {cells['1 3']} {cells['2 3']} {cells['3 3']} |")
                        print(f"| {cells['1 2']} {cells['2 2']} {cells['3 2']} |")
                        print(f"| {cells['1 1']} {cells['2 1']} {cells['3 1']} |")
                        print('---------')
                        turns += 1
                        check_winning()
                        if result():
                            print(result())
                            break
                    else:
                        cells[coordinate] = 'O'
                        print('---------')
                        print(f"| {cells['1 3']} {cells['2 3']} {cells['3 3']} |")
                        print(f"| {cells['1 2']} {cells['2 2']} {cells['3 2']} |")
                        print(f"| {cells['1 1']} {cells['2 1']} {cells['3 1']} |")
                        print('---------')
                        turns += 1
                        check_winning()
                        if result():
                            print(result())
                            break
                else:
                    print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')


