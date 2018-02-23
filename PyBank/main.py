
import csv

Pybudget2 = open("raw_data/budget_data_1.csv")
reader = csv.DictReader(Pybudget2)

for row in reader:
    print(row["Date"])