import Consts
import Solider
import time

guard_loc = [0, Consts.GUARD_Y]
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
        if curr_time - started_time >= 0.5:
            if guard_loc[0] + guard_direction == Consts.FIELD_MATRIX_COLS:
                guard_direction = -1
            elif guard_loc[0] + guard_direction == 0:
                guard_direction = 1
            started_time = time.time()

            guard_loc[0] += guard_direction


def is_caught():
    sol_loc = Solider.get_loc()

    for i in range(sol_loc[1], sol_loc[1] + 4):
        for j in range(sol_loc[0], sol_loc[0] + 1):
            if (j >= guard_loc[0] - 1 and j <= guard_loc[0] + 1) and (i >= Consts.GUARD_Y and i <= Consts.GUARD_Y + 4):
                print("Guard", guard_loc)
                print("Player", Solider.get_loc())
                return True
    return False


def get_guard_loc():
    return guard_loc