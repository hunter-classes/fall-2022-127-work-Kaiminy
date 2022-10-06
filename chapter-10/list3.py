#chapter 10 exercise 5,7,8

#5
def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    print(max)



#7
import random

def countOdd(lst):
    odd = 0
    for e in lst:
        if e % 2 != 0:
            odd = odd + 1
    return odd

# make a random list to test the function
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))

#8
def sumEven(lst):
    # your code here
    even = 0
    for e in lst:
        if e % 2 ==0:
            sum = even + even
    return even

