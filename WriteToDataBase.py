import pandas as pd
import Field
import MineField
import Solider


DF = pd.DataFrame(da)

def create_data_frame():
    portalData = MineField.get_portal_field()
    playerData = Solider.get_loc()
    headData = Field.get_head_field()

    GameData = list(zip())
