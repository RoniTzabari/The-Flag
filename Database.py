import pandas as pd
import MineField
import Field
import Solider


# Read file
def change_game_state(index):
    data = pd.read_csv("GameData.csv", header=0)
    Field.set_head_field(data.Heads[index])
    MineField.set_portal_field(data.Portals[index])
    Solider.set_loc(data.Player[index])


get_game_state(0)