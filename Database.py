import pandas as pd
import MineField
import Field
import Solider


# Read file
def get_game_state(index):
    data = pd.read_csv("GameData.csv", header=0)
    print(data)
    Field.set_head_field(data.Heads[index])
    MineField.set_portal_field(data.Portals[index])
    Solider.set_loc(data.Player[index])
    # game_state = {"field": data.Heads[key_pressed - 1],
    #               "portal_field": data.Portals[key_pressed - 1],
    #               "soldier_loc": data.Player[key_pressed - 1]}


get_game_state(0)