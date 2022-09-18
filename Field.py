import Consts
import Solider
import random

field = []
bush_corner_field = []


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


def get_loc_tup():
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
    loc_tup = (row, col)
    return loc_tup


def generate_bush_field():
    global field, bush_corner_field
    field = new_field()
    bush_corner_field = new_field()

    for i in range(Consts.NUM_OF_OBSTACLES):
        flag = True
        while flag:
            loc = get_loc_tup()
            flag = if_free_for_bush(loc[0], loc[1])

        bush_corner_field[loc[0]][loc[1]] = Consts.BUSH
        for j in range(loc[1], loc[1] + Consts.BUSH_WIDTH):
            for k in range(loc[0], loc[0] + Consts.BUSH_HEIGHT):
                field[k][j] = Consts.BUSH


def if_on_flag():
    location = Solider.get_loc()
    return field[location[0] + 1][location[1]] == Consts.FLAG


def if_free_for_bush(row, col):
    check_str = ''
    for i in range(row, row + Consts.BUSH_HEIGHT):
        for j in range(col, col + Consts.BUSH_WIDTH):
            check_str += field[i][j]
    return check_str == Consts.BUSH * Consts.BUSH_WIDTH * Consts.BUSH_HEIGHT


def get_bush_field():
    return bush_corner_field


generate_bush_field()
print(get_bush_field())
