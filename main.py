def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    is_first = True
    clock = pygame.time.Clock()
    is_run = True
    while is_run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False


        keys_pressed = pygame.key.get_pressed()
        if is_first:
            keys_pressed_last_turn = keys_pressed
            is_first = False
        # movement(keys_pressed, keys_pressed_last_turn)
        red_movement(red, keys_pressed)
        keys_pressed_last_turn = keys_pressed



        draw_window(red, yellow)

    pygame.quit()


if __name__ == '__main__':
    main()