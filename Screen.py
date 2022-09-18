import Consts
import pygame



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
    for i in range(25):

    pass

def index_to_pixels(index):
    return (index[0] * Consts.INDEX_WIDTH, index[1] * Consts.INDEX_HEIGHT)

def update_starter_screen(screen_layout):
    pass


