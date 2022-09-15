import Consts
import Solider
import random

field = []


def new_field():
    empty_field = []
    for i in range(Consts.FIELD_MATRIX_ROWS):
        if i >= Consts.FIELD_MATRIX_ROWS - Consts.FLAG_HEIGHT - 1:
            empty_field.append([
                             Consts.NO_OBSTACLE] * (
                                 Consts.FIELD_MATRIX_COLS - Consts.FLAG_WIDTH)
                             + [Consts.FLAG] * Consts.FLAG_WIDTH)
        else:
            empty_field.append([Consts.NO_OBSTACLE] * Consts.FIELD_MATRIX_COLS)

    return empty_field


def generate_bush_field():
    global field
    field = new_field()
    for i in range(Consts.NUM_OF_OBSTACLES):
        row = random.randint(0, Consts.FIELD_MATRIX_ROWS)
        if row < Consts.SOLDIER_HEIGHT:
            col = random.randint(Consts.SOLDIER_WIDTH,
                                 Consts.FIELD_MATRIX_COLS - Consts.BUSH_WIDTH)
        elif row >= Consts.FIELD_MATRIX_ROWS - Consts.FLAG_HEIGHT - 1:
            col = random.randint(0,
                                 Consts.FIELD_MATRIX_COLS - Consts.FLAG_WIDTH
                                 - Consts.BUSH_WIDTH)
        else:
            col = random.randint(0,
                                 Consts.FIELD_MATRIX_COLS - Consts.BUSH_WIDTH)
        for j in range(col, col + Consts.BUSH_WIDTH):
            field[row][j] = Consts.BUSH


def if_on_flag():
    location = Solider.get_loc()
    return field[location[0] + 1][location[1]] == Consts.FLAG
