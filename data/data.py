import csv
reader=csv.reader(open("billionaires.csv"))
#for line in reader:
  #print (line)

data = [x for x in reader]

d=(data[231],data[129])

print(d)
print(data[0])

import csv
with open('billionaires.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'],'', row['demographics.age'], '', row['rank'])


#with open('billionaires.csv') as f:
    #reader = csv.DictReader(f)
    #for row in reader:
        #list = row['demographics.age']
        
#average = sum(list) / len(list)
       
# Printing average of the list
#print("Average of the list =", average)

print("There are 1565 ranked in this csv")

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot

import csv

x = []
y = []

with open('billionaires.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	
	for row in plots:
		x.append(row[0])
		y.append(int(row[2]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Age")
plt.xlabel('Names')
plt.ylabel('Ages')
plt.title('Ages of different persons')
plt.legend()
plt.show()

