import pandas as pd
import MineField
import Field
import Solider
import os
import ast


DF = pd.DataFrame()
CSV_PATH = "GameData.csv"


def string_to_matrix(string):
    string = string[1:len(string) - 2]
    list = string.split('],')
    list = [x[1::] for x in list]
    final = []
    sub_list = []
    for string in list:
        sub_list = string.split("'")
        sub_list = [x for x in sub_list if sub_list.index(x) % 2 !=0]
        final.append(sub_list)
    return final


# Read file
def change_game_state(index):
    data = pd.read_csv(CSV_PATH)
    Field.set_head_field(string_to_matrix(data.Heads[index]))
    MineField.set_portal_field(string_to_matrix(data.Portals[index]))
    str_list = data.Player[index][1:len(data.Player[index]) - 1].split(', ')
    Solider.set_loc([int(str_list[0]), int(str_list[1])])


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
