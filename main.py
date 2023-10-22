import csv


def calc_decrease(price: float, percentage: float, number_of_years: float) -> float:
    cal_price: float
    final_price: float
    new_price: float
    new_price = price

    for i in range(int(number_of_years)):
        new_price = new_price * 0.80
        final_price = new_price

    return final_price


brand = input("Write the brand of the car : ")

price_new = float(input("Write the amount you bought it for : "))

amount_of_years = float(input("Write amount of years : "))


with open("data.csv", mode="r") as file:
    csv_file = csv.reader(file)

    temp = []

    for i in csv_file:
        temp.append(i)

    if brand in str(temp):
        print(calc_decrease(price_new, 0.20, amount_of_years))
    else:
        print("That brand does not exist in our database, sorry")




