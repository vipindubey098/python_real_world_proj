import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle() #hide turtle, to hide turtle

# colors = ['yellow', 'green', 'blue', 'red']
colors = ['white', 'red', 'white', 'yellow']
for i in range(500):
    for c in colors:
        turtle.color(c)
        turtle.forward(i)
        turtle.left(91)
        turtle.tracer(10)

turtle.mainloop()