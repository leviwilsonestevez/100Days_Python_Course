import pandas as pd

data_squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrels_colors = data_squirrel.pivot_table(columns=['Primary Fur Color'], aggfunc='size')

data_dict = {
    "Fur Color": list(squirrels_colors.to_dict().keys()),
    "Count": list(squirrels_colors.to_dict().values())
}
new_table = pd.DataFrame(data_dict)
new_table.to_csv("squirrel_count.csv")
print(new_table)
