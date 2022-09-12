# open file
import csv
import pandas as pd

file = open('./datasets/all_seasons.csv', 'r')
data = file.read()
# print(repr(data[0:101]))

# this opens file and closes when loop ends


with open('./datasets/all_seasons.csv', 'r') as file:
    data = file.read()

    data_lists = data.split("\n")

    list_of_lists = []
    for line in data_lists:
        row = line.split(',')
        list_of_lists.append(row)

# print(list_of_lists[0:10])

# using csv reader

data_list = list(csv.reader(
    open('./datasets/all_seasons.csv'),  delimiter=','))
# print(data_list[0:10])

subset = data_list[1:301]
count_floats = []

for row in subset:
    count_flo = float(row[4])
    count_floats.append(count_flo)

# print(count_floats[0:5])


# using pandas
df = pd.read_csv('./datasets/all_seasons.csv')

# print(df.head())

del df['Id']

# print(df.head())


with open('./datasets/all_seasons.csv', 'r') as file:
    df = pd.read_csv(file)
del df['Id']

# print(df.head())

# print(df.tail())

print("name with james on data",
      df[df['player_name'] == 'Dennis Rodman'].head())

print(df[(df['player_name'] == 'Dennis Rodman') & (
    df['pts'] > 10) & (df['pts'] < 20)])

print(df.sort_values(by=['pts'], ascending=True).tail(10))
