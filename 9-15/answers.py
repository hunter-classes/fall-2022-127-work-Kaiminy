#question 7
from test import testEqual
def is_even(n):
    if n % 2 == 0:
        print ("true")
    else:
        print ("false")

#question 8
from test import testEqual
def is_odd(n):
    if n % 2 != 0:
        print ("true")
    else:
        print ("false")

#question 10
def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

#question 11
def is_rightangled(a, b, c):
    if a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    elif b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001


#CodingBat- String 1
def hello_name(name):
  return "Hello " + name + "!"


#CodingBat- Make_out_word
def make_out_word(out, word):
  return("<<" + word + ">>")
  return("<<" + word + ">>")
  return("[[" + word + "]]")

#CodingBat- First_two
def first_two(str):
  return str[:2]