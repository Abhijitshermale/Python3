# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# ans=0
# for i in temp_list:
#     ans+=i
# result = ans/len(temp_list)
# print(result)
#
# print(data["temp"].max())
# print(data[data.temp == data["temp"].max()])
#
# data_dict ={
#     "Students": ["Abhijit", "Srushti", "Rahul"],
#     "Scores": [80,90,55]
# }
# d=pandas.DataFrame(data_dict)
# d.to_csv("new_data.csv")
# print(d)

import pandas

data= pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur=len(data[data["Primary Fur Color"]=="Gray"])
red_fur=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_fur=len(data[data["Primary Fur Color"]=="Black"])

data_dict ={
    "Fur Color":["Gray","Cinnamon", "Black"],
    "Count": [gray_fur, red_fur, black_fur]
}
df= pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
