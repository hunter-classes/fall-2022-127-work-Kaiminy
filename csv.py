import csv
reader=csv.reader(open("demo.csv"))
for line in reader:
  print (line)