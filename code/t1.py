import turtle

def sample_function():
  print("This is a function")
  print("It can be used multiple times")


wn= turtle.Screen()

crush = turtle.Turtle()

crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)




#draw a square
for i in range(4):


# create a second turtle
# into the variable squirt
# and make squirt draw a triangle

squirt = turtle.Turtle()

squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("red")
squirt.width(5)
squirt.forward(50)
squirt.forward(120)
squirt.right(50)
squirt.forward(120)


squirt.forward(30)
squirt.right(30)

sample_function()
sample_function()
sample_function()

wn.exitonclick()
wn.mainloop()