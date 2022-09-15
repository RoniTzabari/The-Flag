import Consts
import Field
import Solider
import random

mine_field = []


def generate_mine_field():
    global mine_field
    mine_field = Field.new_field()
    for i in range(Consts.NUM_OF_OBSTACLES):
        flag = True
        while flag:
            loc = Field.get_loc_tup()
            flag = if_free_for_mine(loc[0], loc[1])

        for j in range(loc[1], loc[1] + Consts.MINE_WIDTH):
            mine_field[loc[0]][j] = Consts.MINE


def if_on_mine():
    location = Solider.get_loc()
    right_leg = (location[0] - 3, location[1])
    left_leg = (location[0] - 3, location[1] + 1)
    return (mine_field[right_leg[0]][right_leg[1]] == Consts.MINE or
            mine_field[left_leg[0]][left_leg[1]] == Consts.MINE)


def if_free_for_mine(row, col):
    check_str = ''
    for i in range(row, row + Consts.MINE_WIDTH):
        check_str += mine_field[i, j]
    return check_str == Consts.BUSH * Consts.MINE_WIDTH
