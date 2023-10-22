import csv


with open("data.csv", mode="r") as file:
    csv_file = csv.reader(file)

    for i in csv_file:
        print(i)

