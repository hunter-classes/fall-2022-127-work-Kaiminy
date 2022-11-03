
import random


f = open("story2.py")
contents = f.read()
f.close()


Hero = ["Annabelle", "Hugo", "Trent", "Cynthia", "Sofia", "Nathan", "Amanda", "Algar", "Charlene", "Cleo", "Raquel"]
Verb = ["cook", "dance", "waddle", "swim", "prance", "skip", "hop"]
Noun = ["flowers", "dirty dishes", "cats", "frogs", "nails", "chairs", "pencils", "toothpicks", "homework"]


hero = Hero[random.randint(0,10)]
new_text= contents.replace("<hero>",hero)




for i in new_text:
  new_text=new_text.replace("<noun>", Noun[random.randint(0,8)])


for e in new_text:
  new_text=new_text.replace("<verb>", Verb[random.randint(0,6)])
#if word is "<noun>"

#replace with random choice of word from Noun list
    
  
print(new_text)


for i in new_text:
    temp = str(i)
    temp2 = temp.replace('<noun>',Noun[random.randint(0,8)],2)
    new_text.append(temp2)


for word in new_text:
  new_text= contents.replace("<hero>",hero)

print(new_text)



def contents(n):
  if word == "<noun>"
  contents.replace("<noun>",random.randint(0,8))
print(contents)


for word in new_text:
  if word == "<noun>":
    contents=new_text.replace("<noun>", random.randint(0,8))
  elif word =="<verb>":
    contents=new_text.replace("<verb>", random.randint(0,6))
  else:
    print(contents)



hero = Hero[random.randint(0,10)]
new_text= contents.replace("<hero>",hero)


def noun(Noun):
  noun = Noun[random.randint(0,7)]
  for noun in list:
    new_text=contents.replace("<noun>", noun)
    return new_text



for noun in contents:
  noun = Noun[random.randint(0,7)]
  new_text= contents.replace("<noun>",noun)

def get_word(type, local_dict):
  
  noun = Noun[random.randint(0,7)]
new_text= contents.replace("<noun>",noun)

for i in range(len(Noun)):
  new_noun= "<noun>".replace("<noun>",Noun[random.randint(0,8)])