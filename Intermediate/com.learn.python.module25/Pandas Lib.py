from statistics import mean

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
l_temp = data["temp"].tolist()
print(l_temp)
average_temp = round(mean(l_temp), 2)
print(f"Average Temperature : {average_temp} ")
# Pandas Alternative
average_temp_pandas = round(data["temp"].mean(), 2)
print(f"Average Temperature using Pandas : {average_temp_pandas} ")
max_temp = data["temp"].max()
print(f"Maximun Temperature using Pandas : {max_temp} ")
print(data[data.temp == data.temp.max()])
data["Fahrenheit"] = (data.temp * 1.8) + 32
print(data)

data_new = pandas.DataFrame(data_dict)
data_new.to_csv("new_data.csv")
