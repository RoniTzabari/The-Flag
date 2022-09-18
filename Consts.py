import pygame
import os

FIELD_MATRIX_ROWS = 25
FIELD_MATRIX_COLS = 50

NUM_OF_OBSTACLES = 20
NO_OBSTACLE = 'EMPTY'

MINE = 'MINE'
MINE_WIDTH = 3

BUSH = 'BUSH'
BUSH_WIDTH = 3
BUSH_HEIGHT = 2

FLAG = 'FLAG'
FLAG_WIDTH = 4
FLAG_HEIGHT = 3
FLAG_LOCATION = (21, 46)

SOLDIER_WIDTH = 2
SOLDIER_HEIGHT = 4

STEP = 1

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'


# IMAGES:
HEADS = [pygame.image.load(os.path.join("Bin", "head1.png")),
         pygame.image.load(os.path.join("Bin", "head2.png")),
         pygame.image.load(os.path.join("Bin", "head3.png")),
         pygame.image.load(os.path.join("Bin", "head4.png")),
         pygame.image.load(os.path.join("Bin", "head5.png"))]
PORTAL = pygame.image.load(os.path.join("Bin", "portal.png"))
PLAYER = pygame.image.load(os.path.join("Bin", "rickandmorty.png"))
PLAYER_NIGHT = pygame.image.load(os.path.join("Bin", "rickandmortynight.png"))
BACKGROUND = pygame.image.load(os.path.join("Bin", "space.jpeg"))


# SCREEN:
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
INDEX_WIDTH, INDEX_HEIGHT = 20, 20

pygame.display.set_caption("The Flag")

PLAYER_WIDTH, PLAYER_HEIGHT = INDEX_WIDTH*2, INDEX_HEIGHT*4
HEAD_WIDTH, HEAD_HEIGHT = INDEX_WIDTH*3, INDEX_HEIGHT*2
PORTAL_WIDTH, PORTAL_HEIGHT = INDEX_WIDTH*3, INDEX_HEIGHT*1

BLACK = (0, 0, 0)
LIGHT_GREEN = (16, 222, 19)
BORDER = pygame.Rect(WINDOW / 2, 0, 1, WINDOW_HEIGHT)

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
