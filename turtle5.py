import turtle
b=int(input("shape"))
a = turtle.Turtle()
c=(360/b)

for i in range(b):
    a.forward(100)
    a.left(c)
    
turtle.done()
