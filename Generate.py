import math
from random import randrange

gen_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def index_free(row, col, num):
    for a in range(9):
        if gen_board[a][col] == num:
            return False
    for a in range(9):
        if gen_board[row][a] == num:
            return False
    for a in range(9):
        for b in range(9):
            if math.floor(row/3) == math.floor(a/3) and math.floor(col/3) == math.floor(b/3):
                if gen_board[a][b] == num:
                    return False
    return True


def set_board():
    row = 0
    col = 0
    empty = True
    for x in range(9):
        for y in range(9):
            if gen_board[x][y] == 0:
                row = x
                col = y
                empty = False
                break
        if not empty:
            break
    if empty:
        return True
    for a in range(9):
        count = randrange(1, 10)
        if index_free(row, col, count):
            gen_board[row][col] = count
            if set_board():
                return True
            else:
                gen_board[row][col] = 0
    return False


def clear():
    removed = 81 - 17
    for a in range(removed):
        random_x = randrange(9)
        random_y = randrange(9)
        gen_board[random_x][random_y] = 0


def generate():
    if set_board():
        clear()


