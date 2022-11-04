#the two extras I did were the writing a story in a file to reading it in the program and keeping the hero consistent
#Worked with Irene and Armanndeep 
import random


f = open("story.py")
contents = f.read()
f.close()


Hero = ["Annabelle", "Hugo", "Trent", "Cynthia", "Sofia", "Nathan", "Amanda", "Algar", "Charlene", "Cleo", "Raquel"]
Verb = ["cook", "dance", "waddle", "swim", "prance", "skip", "hop"]
Noun = ["flowers", "dirty dishes", "cats", "frogs", "nails", "chairs", "pencils", "toothpicks", "homework"]


hero = Hero[random.randint(0,10)]
new_text= contents.replace("<hero>",hero)

#I'm sorry but I couldn't figure out the loop and now the code is a really big block and repetitive. The loop is in trial.py but the hero part doesn't work.
for i in new_text:
  new_text=new_text.replace("<noun1>", Noun[random.randint(0,8)])
  new_text=new_text.replace("<noun2>", Noun[random.randint(0,8)])
  new_text=new_text.replace("<noun3>", Noun[random.randint(0,8)])
  new_text=new_text.replace("<noun4>", Noun[random.randint(0,8)])
  new_text=new_text.replace("<noun5>", Noun[random.randint(0,8)])
  new_text=new_text.replace("<noun6>", Noun[random.randint(0,8)])

for e in new_text:
  new_text=new_text.replace("<verb1>", Verb[random.randint(0,6)])
  new_text=new_text.replace("<verb2>", Verb[random.randint(0,6)])
  new_text=new_text.replace("<verb3>", Verb[random.randint(0,6)])
  new_text=new_text.replace("<verb4>", Verb[random.randint(0,6)])
  new_text=new_text.replace("<verb5>", Verb[random.randint(0,6)])
  new_text=new_text.replace("<verb6>", Verb[random.randint(0,6)])
  
#if word is "<noun>"

#replace with random choice of word from Noun list
   
print(new_text)