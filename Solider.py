import MineField
import Field
import Consts

soldier_loc = (0, 0)


def move_soldier(direction):
    if direction == Consts.UP:
        if soldier_loc[0] > 0:
            soldier_loc[0] += Consts.STEP
    elif direction == Consts.DOWN:
        if soldier_loc[0] < Consts.FIELD_MATRIX_ROWS - 1:
            soldier_loc[0] -= Consts.STEP
    elif direction == Consts.RIGHT:
        if soldier_loc[1] > 0:
            soldier_loc[1] += Consts.STEP
    elif direction == Consts.LEFT:
        if soldier_loc[1] < Consts.FIELD_MATRIX_COLS - 1:
            soldier_loc[1] -= Consts.STEP


def get_loc():
    return soldier_loc
