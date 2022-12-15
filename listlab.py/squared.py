#make things squared

def squared(thelist):
  for position in range(len(thelist)):
    thelist[position] = thelist[position] * thelist[position]


numberslist=[5,6,7]
squared(numberslist)
print(numberslist)



#another way to make things squared
numlist=[5,6,7,8]
squaredlist=[num **2 for num in numlist]
print(squaredlist)