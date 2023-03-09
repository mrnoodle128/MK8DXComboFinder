import pandas as pd
import csv
from combination import Combo

CHARACTER_INDEX = 0
BODY_INDEX = 1
WHEEL_INDEX = 2
GLIDER_INDEX = 3
GROUND_SPEED_INDEX = 4
WATER_SPEED_INDEX = 5
AIR_SPEED_INDEX = 6
AG_SPEED_INDEX = 7
ACCELERATION_INDEX = 8
WEIGHT_INDEX = 9
GROUND_HANDLING_INDEX = 10
WATER_HANDLING_INDEX = 11
AIR_HANDLING_INDEX = 12
AG_HANDLING_INDEX = 13
TRACTION_INDEX = 14
MINI_TURBO_INDEX = 15
INVINCIBILITY_INDEX = 16
TOTAL_INDEX = 17

def load_data():
    with open("combinations.csv", "r", newline="") as f:
        csvfile = csv.reader(f)
        raw_combos = list(csvfile)
        return raw_combos


def find_best_of(stat_indexes, raw_combos, tiebreaker):
    current_optimal_combo = ["", 0]
    optimal_combos = []
    for _, combo in enumerate(raw_combos):
        total_important = 0
        for index in stat_indexes:
            total_important += int(combo[index])
        optimal_combo = [combo[CHARACTER_INDEX:GLIDER_INDEX + 1], total_important, int(combo[tiebreaker]), int(combo[TOTAL_INDEX])]
        if optimal_combo[1] > current_optimal_combo[1]:
            current_optimal_combo = optimal_combo
            optimal_combos = [current_optimal_combo]
        elif optimal_combo[1] == current_optimal_combo[1]:
            optimal_combos.append(optimal_combo)


    return optimal_combos

def sort_by_total(e):
    return e[2]

if input("Would you like to create a new file? [y/n] ").upper() == "Y":
    characters_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=0)
    body_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=1)
    wheels_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=2)
    glider_df = pd.read_excel("Mario Kart 8 Stats.xlsx", sheet_name=3)
    combos = []

    for c in range(16):
        for b in range(28):
            for w in range(14):
                for g in range(4):
                    combo = Combo(characters_df.iloc[[c]], body_df.iloc[[b]], wheels_df.iloc[[w]], glider_df.iloc[[g]])
                    combos.append(combo)

    with open("combinations.csv", "w", newline="") as csvfile:
        saveable_combos = []
        for combo in combos:

            saveable_combo = [
                combo.character,
                combo.body,
                combo.wheel,
                combo.glider,
                combo.ground_speed,
                combo.water_speed,
                combo.air_speed,
                combo.ag_speed,
                combo.acceleration,
                combo.weight,
                combo.ground_handling,
                combo.water_handling,
                combo.air_handling,
                combo.ag_handling,
                combo.traction,
                combo.mini_turbo,
                combo.invincibility,
                combo.total
                ]

            saveable_combos.append(saveable_combo)
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(saveable_combos)

else:
    try:
        raw_combos = load_data()
    except FileNotFoundError:
        print("File does not exist")
    
    chosen_stats = []

    while True:
        try:
            chosen_stat = input("Please enter a stat that is important:\n1: Ground Speed\n2: Water Speed\n3: Air Speed\n4: Anti-Gravity Speed\n5: Acceleration\n6: Weight\n7: Ground Handling\n8: Water Handling\n9: Air Handling\n10: Anti-Gravity Handling\n11: Traction\n12: Mini-Turbo\n13: Invincibility\n")
            stat_index = int(chosen_stat) + 3
            if stat_index > 17 or stat_index < 1:
                print("Please enter a value in range")
            else:
                chosen_stats.append(stat_index)
                if input("Do you want to add another stat? [y/n] ").upper() == "Y":
                    pass
                else:
                    break
        except ValueError:
            print("Please enter a number")

    while True:
        try:
            chosen_stat = input("Please enter a stat that you want to sort by:\n1: Ground Speed\n2: Water Speed\n3: Air Speed\n4: Anti-Gravity Speed\n5: Acceleration\n6: Weight\n7: Ground Handling\n8: Water Handling\n9: Air Handling\n10: Anti-Gravity Handling\n11: Traction\n12: Mini-Turbo\n13: Invincibility\n")
            stat_index = int(chosen_stat) + 3
            if stat_index > 17 or stat_index < 1:
                print("Please enter a value in range")
            else:
                sort_stat = stat_index
                break
        except ValueError:
            print("Please enter a number")
            

    best_combos = find_best_of(chosen_stats, raw_combos, sort_stat)
    best_combos.sort(key=sort_by_total)
    for combo in best_combos:
        print(combo)