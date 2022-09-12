import turtle
pirate=turtle.Turtle()
pirate.color("yellow")
    
steps=[160,-43,270,-97,-43,200,-940,17,-86]

#counterclockwise is left

for step in steps:
    pirate.left(90)
    pirate.forward(100)