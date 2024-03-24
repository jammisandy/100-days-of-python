# # with open("Day-25\weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# # import csv
# # with open("Day-25\weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temparatures = []
# #     # for row in data:
# #     #     print(row)
    
# #     for row in data:
# #         if row[1] != "temp":
# #            temparatures.append(int(row[1]))
# #     print(temparatures)


# import pandas
# data = pandas.read_csv("Day-25\weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)

# # #list conversion
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # avg_temp = 0
# # num_items = len(temp_list)
# # for i in temp_list:
# #     avg_temp = avg_temp + i
    
# # print(int(avg_temp/num_items))
# # print(data["temp"].max())
# # print(data["temp"].mean())
# # print(data["temp"].min())
# # print(data["condition"])

# # print(data[data.day == "Monday"])

# # print(data[data.temp == data.temp.max()])


# # monday = data[data.day == "Monday"]
# # print(monday.condition)

# # monday_temp = monday.temp[0]

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [34,56,78]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("New_Data.csv")

import pandas

data = pandas.read_csv("Day-25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240324.csv")
print(data)



