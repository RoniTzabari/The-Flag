import pandas as pd
import MineField
import Field
import Solider
import os


DF = pd.DataFrame()
CSV_PATH = "GameData.csv"


# Read file
def change_game_state(index):
    data = pd.read_csv(CSV_PATH, header=0)
    Field.set_head_field(data.Heads[index])
    MineField.set_portal_field(data.Portals[index])
    Solider.set_loc(data.Player[index])


# Write to file

# USE ONLY THIS OUTSIDE THE MODULE
def insert_game_state(index):
    global DF
    # if file is empty
    if os.stat(CSV_PATH).st_size == 0:
        init_data_frame()
    else:
        DF = pd.read_csv(CSV_PATH, header=0)

    insert_into_dataBase(index)


# if data frame is empty
def init_data_frame():
    global DF
    GameData = {
        "Player": ["None"] * 9,
        "Portals": ["None"] * 9,
        "Heads": ["None"] * 9
    }

    DF = pd.DataFrame(GameData)
    DF["Player"] = DF["Player"].astype('object')
    DF["Portals"] = DF['Portals'].astype('object')
    DF["Heads"] = DF['Heads'].astype('object')


def insert_into_dataBase(index):
    global DF

    playerData = Solider.get_loc()
    portalData = MineField.get_portal_field()
    headData = Field.get_head_field()

    DF.at[index, "Player"] = playerData
    DF.at[index, "Portals"] = portalData
    DF.at[index, "Heads"] = headData

    DF.to_csv(CSV_PATH, index=False)
