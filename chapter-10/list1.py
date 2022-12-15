#chapter 10 exercise 3
myList = [76, 92.3, 'hello', True, 4, 76]

# Your code here
myList.append("apple")
myList.append(76)
myList.insert(0,99)
print(myList.index('hello'))
print(myList.count(76))
mylist.remove(1)
print(myList)
myList.pop(myList.index(True))