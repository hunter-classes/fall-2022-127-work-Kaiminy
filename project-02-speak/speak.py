#The extra that I did was inserting pirate phrases(last bullet point under extras)

file_text = open("input.txt")
s=file_text.read()


dict= { "partner":"laddy parrot",
       "hi":"Avast ye!",
       "here":"high seas",
       "release":"keel-haul", 
       "We":"Us sandcrabs",
       "boat":"ship",
       "beginners":"landlubber scallywags",
       "fixing":"rigging",
       "skill":"cat o' nine tails",
       "release":"belay",
       "here":"yonder there",
       "rest":"finishing piece" }



for i in dict:
  s=s.replace(i,dict[i])


s +="See right here Mateys!"

print(s)