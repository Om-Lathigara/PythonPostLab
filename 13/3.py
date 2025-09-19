import csv
with open("D:\MARWADI\YEAR2\SEM3\python1\data-1.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
