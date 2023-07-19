import csv

with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperatures = []
    for row in data:
        print(row)
        temperatures.append(int(row[1]))
    print(temperatures)
