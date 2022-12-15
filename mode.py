#largest/(smallest?) number
def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    print(max)

def findLargest(dataset):
  largeSoFar = dataset[0]
  for item in dataset[1:]:
    if item > largeSoFar:
      largeSoFar = data
      return largeSoFar




def buildRandomList(size,maxvalue):
  result = []
  for x in range(size):
    result.append(random.randrange(maxvalue))
    return result

    #number 2
    result=[random.randrange(maxvalue) for x in range(size)]
    return result






#finding
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


#finding 2
def freq(dataset,v):
  count = 0
  for item in dataset:
    if item ==v:
      count=count+1
    return count


[x for x in dataset ]



def mode(dataset):
  #frequency of the number in the list
  #returns the most
  #what about multiple high frequencies
  #i don't know
freq = [x for x in dataset]:



modeSoFar = dataset[0]
freqSoFar = freq(dataset,modeSoFar)
for item in dataset[1:]:
  if freq(dataset,item) > freqSoFar:
    modeSoFar = item
    freqSoFar = freq(dataset,item)

return modeSoFar


