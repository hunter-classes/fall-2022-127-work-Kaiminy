def count_letters(s):
  """
  Count the number of times each letter appears in s
  """
  counts={}
  for letter in s:
    if letter in counts.keys():
      counts[letter]=counts[letter]+1
    else:
      counts[letter]=1
  return counts

result = count_letters(s)


def count_words(s):
  counts={}
  for word in s.spilt():
    if word in counts.keys():
      counts[word]=counts[word]+1
    else:
      counts[words]=1
  
  return counts

letter_counts = count_letters(s)
word_counts = count_words(s)