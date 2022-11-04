import random


f = open("story2.py")
contents = f.read()
f.close()


Hero = ["Annabelle", "Hugo", "Trent", "Cynthia", "Sofia", "Nathan", "Amanda", "Algar", "Charlene", "Cleo", "Raquel"]
Verb = ["cook", "dance", "waddle", "swim", "prance", "skip", "hop"]
Noun = ["flowers", "dirty dishes", "cats", "frogs", "nails", "chairs", "pencils", "toothpicks", "homework"]




#I'm sorry but I couldn't figure out the loop and now the code is a really big block and repetitive.

  
#if word is "<noun>"

#replace with random choice of word from Noun list

   


def madlibs(contents):
  new = []
  for word in contents.split():
    new = new + [word.replace("<noun>", random.choice(Noun)).replace('<verb>', random.choice(Verb)).replace("<noun>", random.choice(Noun))]
    result = " ".join(new)
  return result
  return result.replace("<hero>", random.choice(Hero))

print(madlibs(contents))