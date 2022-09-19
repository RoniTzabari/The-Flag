import Consts
import Solider
import time

GUARD_Y = Consts.FIELD_MATRIX_ROWS // 2 - 2  # guard's top left corner
guard_loc = [0, GUARD_Y]
guard_direction = Consts.STEP  # 1 = left, -1 = right
started_time = None


def move_guard():
    global guard_direction
    global guard_loc
    global started_time

    if started_time == None:
        started_time = time.time()
    else:
        curr_time = time.time()
        if curr_time - started_time >= 1.0:
            if guard_loc[0] + guard_direction == Consts.FIELD_MATRIX_COLS:
                guard_direction = -1
            elif guard_loc[0] + guard_direction == 0:
                guard_direction = 1
            started_time = time.time()

            guard_loc[0] += guard_direction


def is_caught():
    sol_loc = Solider.get_loc()
    for i in range(guard_loc[1], guard_loc[1] + 3):
        for j in range(guard_loc[0], guard_loc[0] + 2):
            if [j, i] == sol_loc:
                print("Guard", guard_loc)
                print("Player", Solider.get_loc())
                return True
    return False


def get_guard_loc():
    return guard_loc