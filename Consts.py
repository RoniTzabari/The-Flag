import pygame
import os

FIELD_MATRIX_ROWS = 25
FIELD_MATRIX_COLS = 50

NUM_OF_OBSTACLES = 20
NO_OBSTACLE = 'EMPTY'

PORTAL = 'PORTAL'
PORTAL_WIDTH = 3

TELEPORT = 'TELEPORT'
TELEPORT_WIDTH = PORTAL_WIDTH
TELEPORT_HEIGHT = 2
NUM_OF_TELEPORT = 5


HEAD = 'HEAD'
HEAD_WIDTH = 2
HEAD_HEIGHT = 3

SHIP = 'SHIP'
SHIP_WIDTH = 4
SHIP_HEIGHT = 3
SHIP_LOCATION = (46, 22)

GUARD_Y = FIELD_MATRIX_ROWS // 2 - 2  # guard's top left corner

SOLDIER_WIDTH = 2
SOLDIER_HEIGHT = 4

STEP = 1

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'


# IMAGES:
HEADS_IMG = [pygame.image.load(os.path.join("Bin", "head1.png")),
         pygame.image.load(os.path.join("Bin", "head2.png")),
         pygame.image.load(os.path.join("Bin", "head3.png")),
         pygame.image.load(os.path.join("Bin", "head4.png")),
         pygame.image.load(os.path.join("Bin", "head5.png")),
         pygame.image.load(os.path.join("Bin", "head6.png"))]
PORTAL_IMG = pygame.image.load(os.path.join("Bin", "portal.png"))
PLAYER_IMG = pygame.image.load(os.path.join("Bin", "rickandmorty.png"))
PLAYER_NIGHT_IMG = pygame.image.load(os.path.join("Bin", "rickandmortynight.png"))
BACKGROUND_IMG = pygame.image.load(os.path.join("Bin", "space.jpeg"))
SHIP_IMAGE = pygame.image.load(os.path.join("Bin", "ship.png"))
LOSE_IMAGE = pygame.image.load(os.path.join("Bin", "lose.png"))
WIN_IMAGE = pygame.image.load(os.path.join("Bin", "win.jpg"))
GUARD_IMG = pygame.image.load(os.path.join("Bin", "picklerick.png"))
TELEPORT_IMG = pygame.image.load(os.path.join("Bin", "portal2.png"))


# SCREEN:
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
INDEX_WIDTH, INDEX_HEIGHT = 20, 20

pygame.display.set_caption("The Flag")

PLAYER_WIDTH, PLAYER_HEIGHT = INDEX_WIDTH*2, INDEX_HEIGHT*4
HEAD_WIDTH_IMAGE, HEAD_HEIGHT_IMAGE = INDEX_WIDTH*2, INDEX_HEIGHT*3
PORTAL_WIDTH_IMAGE, PORTAL_HEIGHT_IMAGE = INDEX_WIDTH*3, INDEX_HEIGHT*1
SHIP_WIDTH_IMAGE, SHIP_HEIGHT_IMAGE = SHIP_WIDTH * INDEX_WIDTH, SHIP_HEIGHT * INDEX_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (16, 222, 19)
# BORDER = pygame.Rect(WINDOW / 2, 0, 1, WINDOW_HEIGHT)

FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = 100  # int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = WHITE
LOSE_LOCATION = \
    (0.4 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = WHITE
WIN_LOCATION = \
    (0.3 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
