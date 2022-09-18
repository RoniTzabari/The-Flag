import Consts
import Field
import Solider
import random

portal_field = []
portal_corner_field = []


# def new_field():
#     empty_field = []
#     for i in range(Consts.FIELD_MATRIX_ROWS):
#         if i >= Consts.FIELD_MATRIX_ROWS - Consts.SHIP_HEIGHT - 1:
#             empty_field.append([
#                                    Consts.NO_OBSTACLE] * (
#                                        Consts.FIELD_MATRIX_COLS - Consts.SHIP_WIDTH)
#                                + [Consts.SHIP] * Consts.SHIP_WIDTH)
#         else:
#             empty_field.append([Consts.NO_OBSTACLE] * Consts.FIELD_MATRIX_COLS)
#
#     return empty_field


def generate_portal_field():
    global portal_field, portal_corner_field
    portal_field = Field.new_field()
    portal_corner_field = Field.new_field()
    for i in range(Consts.NUM_OF_OBSTACLES):
        flag = False
        while not flag:
            loc = get_loc_tup()
            flag = if_free_for_portal(loc[0], loc[1])

        portal_corner_field[loc[0]][loc[1]] = Consts.PORTAL
        for j in range(loc[1], loc[1] + Consts.PORTAL_WIDTH):
            portal_field[loc[0]][j] = Consts.PORTAL


def get_loc_tup():
    row = random.randint(0, Consts.FIELD_MATRIX_ROWS - 1)
    if row < Consts.SOLDIER_HEIGHT:
        col = random.randint(Consts.SOLDIER_WIDTH,
                             Consts.FIELD_MATRIX_COLS - Consts.PORTAL_WIDTH)
    elif row >= Consts.FIELD_MATRIX_ROWS - Consts.SHIP_HEIGHT - 1:
        col = random.randint(0,
                             Consts.FIELD_MATRIX_COLS - Consts.SHIP_WIDTH
                             - Consts.PORTAL_WIDTH)
    else:
        col = random.randint(0,
                             Consts.FIELD_MATRIX_COLS - Consts.PORTAL_WIDTH)
    loc_tup = (row, col)
    return loc_tup


def if_on_portal():
    location = Solider.get_loc()
    right_leg = (location[1] + 3, location[0])
    left_leg = (location[1] + 3, location[0] + 1)
    return (portal_field[right_leg[0]][right_leg[1]] == Consts.PORTAL or
            portal_field[left_leg[0]][left_leg[1]] == Consts.PORTAL)


def if_free_for_portal(row, col):
    check_str = ''
    for i in range(col, col + Consts.PORTAL_WIDTH):
        check_str += portal_field[row][i]
    return check_str == Consts.NO_OBSTACLE * Consts.PORTAL_WIDTH


def get_portal_field():
    return portal_corner_field
