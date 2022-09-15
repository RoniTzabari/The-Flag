import Consts
import Field
import Solider
import random

mine_field = []


def generate_mine_field():
    global mine_field
    mine_field = Field.new_field()
    for i in range(Consts.NUM_OF_OBSTACLES):
        row = random.randint(0, Consts.FIELD_MATRIX_ROWS)
        if row < Consts.SOLDIER_HEIGHT:
            col = random.randint(Consts.SOLDIER_WIDTH,
                                 Consts.FIELD_MATRIX_COLS - Consts.MINE_WIDTH)
        elif row >= Consts.FIELD_MATRIX_ROWS - Consts.FLAG_HEIGHT - 1:
            col = random.randint(0,
                                 Consts.FIELD_MATRIX_COLS - Consts.FLAG_WIDTH
                                 - Consts.MINE_WIDTH)
        else:
            col = random.randint(0,
                                 Consts.FIELD_MATRIX_COLS - Consts.MINE_WIDTH)
        for j in range(col, col + Consts.MINE_WIDTH):
            mine_field[row][j] = Consts.MINE


def if_on_mine():
    location = Solider.get_loc()
    right_leg = (location[0] - 3, location[1])
    left_leg = (location[0] - 3, location[1] + 1)
    return (mine_field[right_leg[0]][right_leg[1]] == Consts.MINE or
            mine_field[left_leg[0]][left_leg[1]] == Consts.MINE)
