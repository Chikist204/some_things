import pygame
from random import randint
from copy import deepcopy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size),
                                     1)
                else:
                    pygame.draw.rect(screen, (255, 0, 0), (
                        self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size),
                                     1)


pygame.init()
size = width, height = 1600, 900
tile = 50
w, h = width // tile, height // tile
fps = 20
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
board = Board(tile, tile)
board.set_view(0, 0, 50)

next_field = [[0 for _ in range(w)] for _ in range(h)]
current_field = [[randint(0, 1) for _ in range(w)] for _ in range(h)]


def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    screen.fill(pygame.Color('black'))
    board.render(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if current_field[y][x]:
                pygame.draw.rect(screen, pygame.Color('green'), (x * tile + 2, y * tile - 2, tile - 2, tile - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(fps)