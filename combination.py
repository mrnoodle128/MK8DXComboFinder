import pandas as pd

characters_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=0)
body_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=1)
wheels_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=2)
glider_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=3)


class Combo:
    def __init__(self, character_df, body_df, wheel_df, glider_df):
        self.character = character_df.iloc[0][0]
        self.body = body_df.iloc[0][0]
        self.wheel = wheel_df.iloc[0][0]
        self.glider = glider_df.iloc[0][0]
        
        self.ground_speed = character_df.iloc[0][1] + body_df.iloc[0][1] + wheel_df.iloc[0][1] + glider_df.iloc[0][1]
        self.water_speed = character_df.iloc[0][2] + body_df.iloc[0][2] + wheel_df.iloc[0][2] + glider_df.iloc[0][2]
        self.air_speed = character_df.iloc[0][3] + body_df.iloc[0][3] + wheel_df.iloc[0][3] + glider_df.iloc[0][3]
        self.ag_speed = character_df.iloc[0][4] + body_df.iloc[0][4] + wheel_df.iloc[0][4] + glider_df.iloc[0][4]
        self.acceleration = character_df.iloc[0][5] + body_df.iloc[0][5] + wheel_df.iloc[0][5] + glider_df.iloc[0][5]
        self.weight = character_df.iloc[0][6] + body_df.iloc[0][6] + wheel_df.iloc[0][6] + glider_df.iloc[0][6]
        self.ground_handling = character_df.iloc[0][7] + body_df.iloc[0][7] + wheel_df.iloc[0][7] + glider_df.iloc[0][7]
        self.water_handling = character_df.iloc[0][8] + body_df.iloc[0][8] + wheel_df.iloc[0][8] + glider_df.iloc[0][8]
        self.air_handling = character_df.iloc[0][9] + body_df.iloc[0][9] + wheel_df.iloc[0][9] + glider_df.iloc[0][9]
        self.ag_handling = character_df.iloc[0][10] + body_df.iloc[0][10] + wheel_df.iloc[0][10] + glider_df.iloc[0][10]
        self.traction = character_df.iloc[0][11] + body_df.iloc[0][11] + wheel_df.iloc[0][11] + glider_df.iloc[0][11]
        self.mini_turbo = character_df.iloc[0][12] + body_df.iloc[0][12] + wheel_df.iloc[0][12] + glider_df.iloc[0][12]
        self.invincibility = character_df.iloc[0][13] + body_df.iloc[0][13] + wheel_df.iloc[0][13] + glider_df.iloc[0][13]
        self.total = self.ground_speed + self.water_speed + self.air_speed + self.ag_speed + self.acceleration + self.weight + self.ground_handling + self.water_handling + self.air_handling + self.ag_handling + self.traction + self.mini_turbo + self.invincibility