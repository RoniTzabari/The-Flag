import pygame
import Consts
import MineField
import Solider
import Screen
import Field

def is_win_or_lose():
    check = True
    if MineField.if_on_portal():
        Screen.draw_lose_message()
        check = False
    elif Field.if_on_ship():
        Screen.draw_win_message()
        check = False
    return check

def which_number_is_pressed(keys_pressed):
    pressed_num = 0
    if keys_pressed[pygame.K_1]:
        pressed_num = pygame.K_1
    elif keys_pressed[pygame.K_2]:
        pressed_num = pygame.K_2
    elif keys_pressed[pygame.K_3]:
        pressed_num = pygame.K_3
    elif keys_pressed[pygame.K_4]:
        pressed_num = pygame.K_4
    elif keys_pressed[pygame.K_5]:
        pressed_num = pygame.K_5
    elif keys_pressed[pygame.K_6]:
        pressed_num = pygame.K_6
    elif keys_pressed[pygame.K_7]:
        pressed_num = pygame.K_7
    elif keys_pressed[pygame.K_8]:
        pressed_num = pygame.K_8
    elif keys_pressed[pygame.K_9]:
        pressed_num = pygame.K_9
    return pressed_num

def check_if_save_or_open(pressed_num):
    ticks=pygame.time.get_ticks()
    keys_pressed = pygame.key.get_pressed()
    while keys_pressed[pressed_num]:
        keys_pressed = pygame.key.get_pressed()
    if (pygame.time.get_ticks() - ticks) <= 1000:
        print("save game")
    else:
        print("open game")


def main():
    MineField.generate_portal_field()
    Field.generate_head_field()
    is_first = True
    clock = pygame.time.Clock()
    is_run = True
    while is_run:
        clock.tick(Consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False

        Screen.update_starter_screen()

        keys_pressed = pygame.key.get_pressed()
        pressed_num = which_number_is_pressed()
        if pressed_num != 0:
            check_if_save_or_open(pressed_num)
        if is_first:
            keys_pressed_last_turn = keys_pressed
            is_first = False
        Solider.move_soldier(Screen.movement(keys_pressed, keys_pressed_last_turn))
        keys_pressed_last_turn = keys_pressed

        is_run = is_win_or_lose()

    pygame.time.wait(3000)
    pygame.quit()


if __name__ == '__main__':
    main()