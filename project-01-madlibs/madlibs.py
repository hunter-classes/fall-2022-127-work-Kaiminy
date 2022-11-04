#the two extras I did were the writing a story in a file to reading it in the program and keeping the hero consistent
#Worked with Irene and Armanndeep 
import random


f = open("story.py")
contents = f.read()
f.close()


Hero = ["Annabelle", "Hugo", "Trent", "Cynthia", "Sofia", "Nathan", "Amanda", "Algar", "Charlene", "Cleo", "Raquel"]
Verb = ["cook", "dance", "waddle", "swim", "prance", "skip", "hop"]
Noun = ["flowers", "dirty dishes", "cats", "frogs", "nails", "chairs", "pencils", "toothpicks", "homework"]


def madlibs(contents):
  new = []
  for word in contents.split():
    new = new + [word.replace("<noun>", random.choice(Noun)).replace('<verb>', random.choice(Verb)).replace("<noun>", random.choice(Noun))]
    result = " ".join(new)
    result= result.replace("<hero>",random.choice(Hero))
  return result

printmadlibs(contents)