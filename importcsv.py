import csv

header=[]
rows=[]

with open('D:\Learning\Python\Sample_DataSet1.csv', newline='') as file:

    csvreader=csv.reader(file)
    header=next(csvreader)      
    for row in csvreader:
        rows.append(row)
    l=len(rows)
for i in range(l):
    print(rows[i][0])