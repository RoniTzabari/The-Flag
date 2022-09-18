import Consts
import pygame
import Field
import MineField
import Solider
import random

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
    # create horizontal lines
    for i in range(1, 25):
        rect = pygame.Rect((0, i * Consts.INDEX_WIDTH), (1, Consts.WINDOW_HEIGHT))
        pygame.draw.rect(WINDOW, Consts.LIGHT_GREEN, rect)

    # putting portals
    mine_fiels = MineField.get_portal_field()
    for i in range(len(mine_fiels)):
        if i == Consts.PORTAL_IMG:
            portal = pygame.Rect(index_to_pixels(mine_fiels.index(i)), (Consts.PORTAL_WIDTH_IMAGE, Consts.PORTAL_HEIGHT_IMAGE))
            render_portal(portal)

    pygame.display.update()
    pygame.time.wait(1000)


def index_to_pixels(index):
    return (index[0] * Consts.INDEX_WIDTH, index[1] * Consts.INDEX_HEIGHT)


def update_starter_screen():
    WINDOW.blit(Consts.BACKGROUND_IMG, (0, 0))

    player_index = Solider.get_loc()
    field_layout = Field.get_head_field()

    # putting heads
    for i in field_layout():
        if i == Consts.HEAD:
            head = pygame.Rect(index_to_pixels(field_layout.index(i)), (Consts.HEAD_WIDTH_IMAGE, Consts.HEAD_HEIGHT_IMAGE))
            render_head(head)
        if i == Consts.SHIP:
            ship = pygame.Rect(index_to_pixels(Consts.SHIP_LOCATION), (Consts.SHIP_WIDTH, Consts.SHIP_HEIGHT))
            WINDOW.blit(Consts.SHIP_IMG, (ship.x, ship.y))

    player = pygame.Rect(index_to_pixels(player_index), (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(Consts.PLAYER_IMG, (player.x, player.y))

    pygame.display.update()


def render_portal(portal):
    WINDOW.blit(Consts.PORTAL, (portal.x, portal.y))


def render_head(head):
    WINDOW.blit(get_random_head(), (head.x, head.y))


def get_random_head():
    index = random.randint(0, 6)
    return Consts.HEADS_IMG[index]


# WIN LOSE
def draw_lose_message():
    draw_message(Consts.LOSE_MESSAGE, Consts.LOSE_FONT_SIZE,
                 Consts.LOSE_COLOR, Consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(Consts.WIN_MESSAGE, Consts.WIN_FONT_SIZE,
                 Consts.WIN_COLOR, Consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    Consts.WINDOW.blit(text_img, location)