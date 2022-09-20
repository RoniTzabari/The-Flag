import Consts
import pygame
import Field
import MineField
import Solider
import random
import Guard

WINDOW = Consts.WINDOW


def movement(keys_pressed, keys_pressed_last_turn):
    direction = ""

    if (keys_pressed[pygame.K_a] and not keys_pressed_last_turn[pygame.K_a]) or (keys_pressed[pygame.K_LEFT] and not keys_pressed_last_turn[pygame.K_LEFT]):  # LEFT
        direction = Consts.LEFT
    elif (keys_pressed[pygame.K_d] and not keys_pressed_last_turn[pygame.K_d]) or (keys_pressed[pygame.K_RIGHT] and not keys_pressed_last_turn[pygame.K_RIGHT]):  # RIGHT
        direction = Consts.RIGHT
    elif (keys_pressed[pygame.K_w] and not keys_pressed_last_turn[pygame.K_w]) or (keys_pressed[pygame.K_UP] and not keys_pressed_last_turn[pygame.K_UP]):  # UP
        direction = Consts.UP
    elif (keys_pressed[pygame.K_s] and not keys_pressed_last_turn[pygame.K_s]) or (keys_pressed[pygame.K_DOWN] and not keys_pressed_last_turn[pygame.K_DOWN]):  # DOWN
        direction = Consts.DOWN
    elif keys_pressed[pygame.K_RETURN] and not keys_pressed_last_turn[pygame.K_RETURN]:  # ENTER
        create_night_screen()
        return ""
    return direction


def create_night_screen():
    WINDOW.fill(Consts.BLACK)

    player_index = Solider.get_loc()
    guard_index = Guard.get_guard_loc()

    # create vertical lines
    for i in range(1, Consts.FIELD_MATRIX_COLS):
        rect = pygame.Rect((i * Consts.INDEX_WIDTH, 0), (1, Consts.WINDOW_HEIGHT))
        pygame.draw.rect(WINDOW, Consts.LIGHT_GREEN, rect)
    # create horizontal linesa
    for i in range(1, Consts.FIELD_MATRIX_ROWS):
        rect = pygame.Rect((0, i * Consts.INDEX_WIDTH), (Consts.WINDOW_WIDTH, 1))
        pygame.draw.rect(WINDOW, Consts.LIGHT_GREEN, rect)

    # putting portals
    mine_fiels = MineField.get_portal_field()
    for i in range(Consts.FIELD_MATRIX_ROWS):
        for j in range(Consts.FIELD_MATRIX_COLS):
            if mine_fiels[i][j] == Consts.PORTAL:
                portal_data = pygame.transform.scale(Consts.PORTAL_IMG, (Consts.PORTAL_WIDTH_IMAGE, Consts.PORTAL_HEIGHT_IMAGE))
                portal = pygame.Rect(index_to_pixels((j, i)), (Consts.PORTAL_WIDTH_IMAGE, Consts.PORTAL_HEIGHT_IMAGE))
                render_portal(portal, portal_data)
            if mine_fiels[i][j] == Consts.TELEPORT:
                teleport_data = pygame.transform.scale(Consts.TELEPORT_IMG, (Consts.PORTAL_WIDTH_IMAGE, Consts.PORTAL_HEIGHT_IMAGE))
                teleport = pygame.Rect(index_to_pixels((j, i)), (Consts.PORTAL_WIDTH_IMAGE, Consts.PORTAL_HEIGHT_IMAGE))
                render_portal(teleport, teleport_data)

    player_data = pygame.transform.scale(Consts.PLAYER_NIGHT_IMG, (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    player = pygame.Rect(index_to_pixels(player_index), (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(player_data, (player.x, player.y))

    guard_data = pygame.transform.scale(Consts.GUARD_NIGHT_IMG, (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    guard = pygame.Rect(index_to_pixels(guard_index), (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(guard_data, (guard.x, guard.y))

    pygame.display.update()
    pygame.time.wait(1000)


def index_to_pixels(index):
    return (index[0] * Consts.INDEX_HEIGHT, index[1] * Consts.INDEX_WIDTH)


def update_starter_screen():
    WINDOW.blit(Consts.BACKGROUND_IMG, (0, 0))

    player_index = Solider.get_loc()
    field_layout = Field.get_head_field()
    guard_index = Guard.get_guard_loc()

    # putting heads
    for i in range(Consts.FIELD_MATRIX_ROWS):
        for j in range(Consts.FIELD_MATRIX_COLS):
            if field_layout[i][j] == Consts.HEAD:
                head_data = pygame.transform.scale(get_random_head(),
                                                   (Consts.HEAD_WIDTH_IMAGE, Consts.HEAD_HEIGHT_IMAGE))
                head = pygame.Rect(index_to_pixels((j, i)),
                                   (Consts.HEAD_WIDTH_IMAGE, Consts.HEAD_HEIGHT_IMAGE))
                render_head(head, head_data)

    ship_data = pygame.transform.scale(Consts.SHIP_IMAGE, (Consts.SHIP_WIDTH_IMAGE, Consts.SHIP_HEIGHT_IMAGE))
    ship = pygame.Rect(index_to_pixels(Consts.SHIP_LOCATION), (Consts.SHIP_WIDTH_IMAGE, Consts.SHIP_HEIGHT_IMAGE))
    WINDOW.blit(ship_data, (ship.x, ship.y))

    player_data = pygame.transform.scale(Consts.PLAYER_IMG, (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    player = pygame.Rect(index_to_pixels(player_index), (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(player_data, (player.x, player.y))

    guard_data = pygame.transform.scale(Consts.GUARD_IMG, (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    guard = pygame.Rect(index_to_pixels(guard_index),(Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(guard_data, (guard.x, guard.y))

    pygame.display.update()


def render_portal(portal, portal_data):
    WINDOW.blit(portal_data, (portal.x, portal.y))


def render_head(head, data):
    WINDOW.blit(data, (head.x, head.y))


def get_random_head():
    index = random.randint(0, 5)
    return Consts.HEADS_IMG[index]


# WIN LOSE
def draw_lose_message():
    draw_message(Consts.LOSE_MESSAGE, Consts.LOSE_FONT_SIZE,
                 Consts.LOSE_COLOR, Consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(Consts.WIN_MESSAGE, Consts.WIN_FONT_SIZE,
                 Consts.WIN_COLOR, Consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    pygame.font.init()

    WINDOW.blit(Consts.BACKGROUND_IMG, (0, 0))

    if message == "You Lost!":
        img_data = pygame.transform.scale(Consts.LOSE_IMAGE, (315, 270))
        img = pygame.Rect((50, 100), (315, 270))
        WINDOW.blit(img_data, (img.x, img.y))
    elif message == "You Won!":
        img_data = pygame.transform.scale(Consts.WIN_IMAGE, (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        img = pygame.Rect((0, 0), (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        WINDOW.blit(img_data, (0, 0))

    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    WINDOW.blit(text_img, location)

    pygame.display.update()