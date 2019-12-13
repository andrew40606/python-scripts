def print_figure(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    return
board = {'top-L':' ', 'top-M':' ', 'top-R':' ', 'mid-L':' ', 'mid-M':' ', 'mid-R':' ', 'low-L':' ', 'low-M':' ', 'low-R':' '}
print('Build a tictactoe board!')
while ' ' in board.values():
    pos = input('position =')
    if pos in board:
        elem = input('O or X? ')
        if elem == 'O' or elem == 'X':
            board[pos] = elem
        else:
            print('please enter a correct format')
    else:
        print('please enter a correct format')
    print_figure(board)

