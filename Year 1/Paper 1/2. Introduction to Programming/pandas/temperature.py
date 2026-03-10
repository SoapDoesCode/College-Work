import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./datasets/temperature.csv")

def filter_data(data: pd.DataFrame, column, target) -> pd.DataFrame:
    filtered = data[data[column]==target]
    return filtered

while True:
    try:
        try:
            user_column = input("Which column would you like to filter by?\nColumn: ")
            if user_column not in df.columns:
                raise KeyError
        except KeyError:
            print("That column does not exist, please try again")
            continue

        try:
            user_target = input(f"Which {user_column} would you like to filter for?\n{user_column}: ")
            if "." in user_target:
                user_target = float(user_target)
            elif user_target.isdigit():
                user_target = int(user_target)
            else:
                pass
        except ValueError:
            pass
    
            print(filter_data(df, user_column, user_target))
    except (EOFError, KeyboardInterrupt):
        print("PLEASE STOP THAT, YOU'VE DONE THIS ENOUGH ALREADY 😭")
        continue