import csv
import pandas


def raw_csv():
    with open("weather_data.csv", "r") as raw_weather:
        weather = csv.reader(raw_weather)
        next(weather)
        temperatures = []
        for w in weather:
            temperatures.append(int(w[1]))
        print(temperatures)


def with_pandas():
    weather = pandas.read_csv("weather_data.csv")
    temps = weather["temp"].to_list()
    average_temp = sum(temps) / len(temps)
    print(average_temp)


def simpler():
    weather = pandas.read_csv("weather_data.csv")
    monday = weather[weather.day == "Monday"]
    temper = (monday.temp * 1.8000) + 32
    print(temper)


def count_squirrels_by_color():
    squirrels = pandas.read_csv("squirrel_data.csv")
    gray = len(squirrels[squirrels["Primary Fur Color"] == "Gray"].index)
    red = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"].index)
    black = len(squirrels[squirrels["Primary Fur Color"] == "Black"].index)
    squirrel_colors = {
        "Color": ["gray", "red", "black"],
        "Count": [gray, red, black],
    }
    data_frame = pandas.DataFrame(data=squirrel_colors)
    data_frame.to_csv("squirrel_colors.csv")


count_squirrels_by_color()

