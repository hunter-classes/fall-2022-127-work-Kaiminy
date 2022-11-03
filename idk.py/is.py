
import random


f = open("story.py")
contents = f.read()
f.close()


Hero = ["Annabelle", "Hugo", "Trent", "Cynthia", "Sofia", "Nathan", "Amanda", "Algar", "Charlene", "Cleo", "Raquel"]
Verb = ["cook", "dance", "waddle", "swim", "prance", "skip", "hop"]
Noun = ["flowers", "dirty dishes", "cats", "frogs", "nails", "chairs", "pencils", "toothpicks", "homework"]


hero = Hero[random.randint(0,10)]
new_text= contents.replace("<hero>",hero)

noun = Noun[random.randint(0,8)]
result=new_text.replace("<noun>",noun)

verb = Verb[random.randint(0,6)]
final=result.replace("<verb>",verb)

print(final)