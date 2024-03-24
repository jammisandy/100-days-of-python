import pandas
data = pandas.read_csv("Day-25/2018_cental.csv")
gray_squirel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirel_count)
print(red_squirel_count)
print(black_squirel_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirel_count, red_squirel_count, black_squirel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")