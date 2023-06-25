import random

board = [['0'] * 5 for i in range(5)]


def print_board(board):
    for row in board:
        print(''.join(row))


print('Мокской бой')
print_board(board)


def random_row(board):
    return random.randint(0, len(board) - 1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turm in range(4):
    print('Ход', turm + 1)
    quess_row = int(input('0-4: '))
    quess_col = int(input('0-4: '))

    if quess_row == ship_row and quess_col == ship_col:
        print('WIN')
        break
    else:
        if (quess_row < 0 or quess_row > 4) or (quess_col < 0 or quess_col > 4):
            print('Выберите допустимое значение: 0-4')
        elif board[quess_row][quess_col] == 'x':
            print('NO')
        else:
            print("Not")
            board[quess_row][quess_col] = 'x'
            if turm == 3:
                print('END GAME')
        print_board(board)