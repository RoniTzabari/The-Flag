import pygame
import Consts
import MineField
import Solider
import Screen
import Field



def main():

    is_first = True
    clock = pygame.time.Clock()
    is_run = True
    while is_run:
        clock.tick(Consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False


        keys_pressed = pygame.key.get_pressed()
        if is_first:
            keys_pressed_last_turn = keys_pressed
            is_first = False
        Screen.movement(keys_pressed, keys_pressed_last_turn)
        keys_pressed_last_turn = keys_pressed




    pygame.quit()


if __name__ == '__main__':
    main()