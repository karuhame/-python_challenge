# import csv
# with open("./day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(row[1])        
#     print(temp)
import pandas
data = pandas.read_csv("./day25/weather_data.csv") #series and dataFrame
# print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(data.temp)
# print(data["temp"].max()) 

# Get data in column
print(data.day)

#Get data in row
print(data.tail(8))
print(data[0:5])
# data.day: nội dung của ô trong cột day
print((data[data.day == "Monday"]).condition)

monday = data[data.day == "Monday"]
print(monday.condition)