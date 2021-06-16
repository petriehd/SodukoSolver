import math
import pygame
from Classes import *
from Generate import *
import time

board =     [
    [5, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 7, 0, 9, 4, 0, 0, 1],
    [0, 6, 0, 0, 7, 5, 0, 0, 0],
    [4, 0, 3, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 2, 0, 6],
    [0, 0, 0, 2, 3, 0, 0, 5, 0],
    [6, 0, 0, 5, 4, 0, 9, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 7]
]
board_empty = [
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


def is_valid(row, col, num):
    for a in range(9):
        if board[a][col] == num:
            return False
    for b in range(9):
        if board[row][b] == num:
            return False
    for a in range(9):
        for b in range(9):
            if math.floor(row/3) == math.floor(a/3) and math.floor(col/3) == math.floor(b/3):
                if board[a][b] == num:
                    return False
    return True


def solve():
    row = 0
    col = 0
    is_empty = True
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                row = x
                col = y
                is_empty = False
                break
        if not is_empty:
            break
    if is_empty:
        return True
    for count in range(1, 10):
        if is_valid(row, col, count):
            board[row][col] = count
            if solve():
                return True
            else:
                board[row][col] = 0
    return False


def solve_steps():
    row = 0
    col = 0
    is_empty = True
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                row = x
                col = y
                is_empty = False
                break
        if not is_empty:
            break
    if is_empty:
        return True
    for count in range(1, 10):
        if is_valid(row, col, count):
            board[row][col] = count
            screen.fill((200, 200, 200))
            screen.blit(grid, (10, 10))
            show_board()
            pygame.display.flip()
            time.sleep(0.1)
            if solve_steps():
                return True
            else:
                board[row][col] = 0
    return False


def show_board():
    current_x = 32.5
    current_y = 30
    for a in board:
        value = font.render('  '.join(str(b)for b in a), True, (13, 13, 13))
        screen.blit(value, (current_x, current_y))
        current_y += 46


# Set window and load
pygame.init()
screen = pygame.display.set_mode((500, 600))
background = pygame.Surface((450, 450))
grid = pygame.image.load('Sodukogrid.png')
font = pygame.font.Font('freesansbold.ttf', 42)

# Initialise buttons
new_button = button((255, 255, 255), 25, 450, 120, 25, 'New Board')
isolve_button = button((255,255,255), 150, 450, 150, 25, 'Instant Solve')
ssolve_button = button((255, 255, 255), 305, 450, 120, 25, 'Show solve')


# Set Caption and Icon
pygame.display.set_caption("Soduko Master")
icon = pygame.image.load('Soduko.png')
pygame.display.set_icon(icon)

# Run
running = True
while running:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if new_button.on_button(pos):
                generate()
                board = gen_board
            if isolve_button.on_button(pos):
                solve()
                show_board()
            if ssolve_button.on_button(pos):
                solve_steps()
                show_board()

    screen.fill((200, 200, 200))
    screen.blit(grid, (10, 10))
    show_board()
    new_button.draw(screen)
    isolve_button.draw(screen)
    ssolve_button.draw(screen)
    pygame.display.update()







