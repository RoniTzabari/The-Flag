import Consts
import Solider
import random
import MineField

field = []
head_corner_field = []


def new_field():
    empty_field = []
    for i in range(Consts.FIELD_MATRIX_ROWS):
        if i >= Consts.FIELD_MATRIX_ROWS - Consts.SHIP_HEIGHT - 1:
            empty_field.append([
                                   Consts.NO_OBSTACLE] * (
                                       Consts.FIELD_MATRIX_COLS - Consts.SHIP_WIDTH)
                               + [Consts.SHIP] * Consts.SHIP_WIDTH)
        else:
            empty_field.append([Consts.NO_OBSTACLE] * Consts.FIELD_MATRIX_COLS)

    return empty_field


def get_loc_tup():
    row = random.randint(0, Consts.FIELD_MATRIX_ROWS - Consts.HEAD_HEIGHT)
    if row < Consts.SOLDIER_HEIGHT:
        col = random.randint(Consts.SOLDIER_WIDTH,
                             Consts.FIELD_MATRIX_COLS - Consts.HEAD_WIDTH)
    elif row >= Consts.FIELD_MATRIX_ROWS - Consts.SHIP_HEIGHT - 1:
        col = random.randint(0,
                             Consts.FIELD_MATRIX_COLS - Consts.SHIP_WIDTH
                             - Consts.HEAD_WIDTH)
    else:
        col = random.randint(0,
                             Consts.FIELD_MATRIX_COLS - Consts.HEAD_WIDTH)
    loc_tup = (row, col)
    return loc_tup


def generate_head_field():
    global field, head_corner_field
    field = new_field()
    head_corner_field = new_field()

    for i in range(Consts.NUM_OF_OBSTACLES):
        flag = True
        while flag:
            loc = get_loc_tup()
            flag = if_free_for_head(loc[0], loc[1])

        head_corner_field[loc[0]][loc[1]] = Consts.HEAD
        for j in range(loc[1], loc[1] + Consts.HEAD_WIDTH):
            for k in range(loc[0], loc[0] + Consts.HEAD_HEIGHT):
                field[k][j] = Consts.HEAD


def if_on_ship():
    location = Solider.get_loc()
    return field[location[0] + 1][location[1]] == Consts.SHIP


def if_free_for_head(row, col):
    check_str = ''
    x = row + Consts.HEAD_HEIGHT
    y = col + Consts.HEAD_WIDTH
    z = 0
    for i in range(row, x):
        for j in range(col, y):
            z += 1
            if z == 7:
                break
            check_str += field[i][j]
    return check_str == Consts.HEAD * Consts.HEAD_WIDTH * Consts.HEAD_HEIGHT


def get_head_field():
    return head_corner_field
