def piglatin():
  word=input("Enter a word")
  for word in word:
    print(word(1:)) + word(:1)

if word(0:)=[a,e,i,o,u]:
  print(word)+"yay"

elif word(1:)!=[b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z]
  print(word(1:))+word(:1)




#bondify
def bondify
firstname=input("What is your first name")
lastname=input("What is your last name")

print(lastname + "," +firstname)



#piglatin classwork

def piglatinify(word):
  first = word[0]
  if first == 'a' or first == 'e'






#piglatin classwork
  def piglatinify(word):
    
    first = word[0]
    if first in 'aeiou':
        result = word + 'ay'
    else:
        # move first letter to end and add 'ay'
        result = word[1:]+first+'ay'
    
    return result
