import Consts
import MineField
import Solider
import random


def if_free_for_teleport(row, col, mine_field):
    check_str = ''
    for i in range(row - 1, row + 1):
        for j in range(col, col + Consts.TELEPORT_WIDTH):
            check_str += mine_field[i][j]
    return check_str == Consts.NO_OBSTACLE * Consts.TELEPORT_HEIGHT * Consts.TELEPORT_WIDTH and row < 20 and row > 4


def teleport_start_index(loc):
    portal_field = MineField.get_full_portal_field()
    if loc[1] == 0:
        return loc
    elif loc[1] == 1:
        if portal_field[loc[0]][loc[1] - 1] == Consts.TELEPORT:
            return [loc[0], loc[1] - 1]
        else:
            return loc
    else:
        for i in range(loc[1] - 2, loc[1]):
            if portal_field[loc[0]][loc[1] - 1] == Consts.TELEPORT:
                return [loc[0], i]
    return loc


def if_on_teleport():
    portal_field = MineField.get_full_portal_field()
    location = Solider.get_loc()
    right_leg = [location[1] + 3, location[0]]
    left_leg = [location[1] + 3, location[0] + 1]
    teleport_start = ""
    if portal_field[right_leg[0]][right_leg[1]] == Consts.TELEPORT:
        teleport_start = teleport_start_index([right_leg[0], right_leg[1]])
    elif portal_field[left_leg[0]][left_leg[1]] == Consts.TELEPORT:
        teleport_start = teleport_start_index([left_leg[0], left_leg[1]])
    if teleport_start != "":
        portal_corner_field = MineField.get_portal_field()
        teleport_num = random.randint(0, Consts.NUM_OF_TELEPORT - 2)
        count = 0
        for i in range(4, len(portal_corner_field) - 4):
            for j in range(len(portal_corner_field[i])):
                if portal_corner_field[i][j] == Consts.TELEPORT:
                    if portal_corner_field[i][j] == Consts.TELEPORT and \
                            [i, j] != teleport_start:
                        if count == teleport_num:
                            sol_loc = [j, i - 4]
                        count += 1
        Solider.set_loc(sol_loc)
        print(sol_loc)
