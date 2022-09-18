import Consts
import pygame
import Field
import MineField

WINDOW = Consts.WINDOW


def movement(keys_pressed, keys_pressed_last_turn):
    direction = ""
    if keys_pressed[pygame.K_KP_ENTER] and not keys_pressed_last_turn[pygame.K_KP_ENTER]:
        create_night_screen()
        return ""
    elif keys_pressed[pygame.K_a] and not keys_pressed_last_turn[pygame.K_a]:  # LEFT
        direction = Consts.LEFT
    elif keys_pressed[pygame.K_d] and keys_pressed_last_turn[pygame.K_d]:  # RIGHT
        direction = Consts.RIGHT
    elif keys_pressed[pygame.K_w] and keys_pressed_last_turn[pygame.K_w]:  # UP
        direction = Consts.UP
    elif keys_pressed[pygame.K_s] and keys_pressed_last_turn[pygame.K_s]:  # DOWN
        direction = Consts.DOWN
    return direction


def create_night_screen():
    # create vertical lines
    for i in range(1, 50):
        rect = pygame.Rect((i * Consts.INDEX_WIDTH, 0), (1, Consts.WINDOW_HEIGHT))
        pygame.draw.rect(WINDOW, Consts.LIGHT_GREEN, rect)
    # create horisontal lines
    for i in range(1, 25):
        rect = pygame.Rect((0, i * Consts.INDEX_WIDTH), (1, Consts.WINDOW_HEIGHT))
        pygame.draw.rect(WINDOW, Consts.LIGHT_GREEN, rect)

    # putting portals
    mine_fiels = MineField.get_mine_field()
    for i in range(len(mine_fiels)):
        if i == Consts.BUSH:
            portal = pygame.Rect(index_to_pixels(mine_fiels.index(i)), (Consts.PORTAL_WIDTH, Consts.PORTAL_HEIGHT))
            render_portal(portal)


def index_to_pixels(index):
    return (index[0] * Consts.INDEX_WIDTH, index[1] * Consts.INDEX_HEIGHT)


def update_starter_screen(screen_layout):
    pass


def render_portal(portal):
    WINDOW.blit(Consts.PORTAL, (portal.x, portal.y))

def render_heads():
    pass