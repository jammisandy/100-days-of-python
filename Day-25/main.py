# with open("Day-25\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("Day-25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparatures = []
#     # for row in data:
#     #     print(row)
    
#     for row in data:
#         if row[1] != "temp":
#            temparatures.append(int(row[1]))
#     print(temparatures)


import pandas
data = pandas.read_csv("Day-25\weather_data.csv")
print(data["temp"])


