import pygame
import Consts
import MineField
import Solider
import Screen
import Field

# def is_win_or_lose():
#     check = True
#     if MineField.if_on_mine():
#         Screen.draw_lose_message()
#         check = False
#     elif Field.if_on_flag():
#         Screen.draw_win_message()
#         check = False
#     return check


def main():
    MineField.generate_mine_field()
    Field.generate_bush_field()
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
        if is_first:
            keys_pressed_last_turn = keys_pressed
            is_first = False
        Solider.move_soldier(Screen.movement(keys_pressed, keys_pressed_last_turn))
        keys_pressed_last_turn = keys_pressed

        #is_run = is_win_or_lose()







    pygame.quit()


if __name__ == '__main__':
    main()