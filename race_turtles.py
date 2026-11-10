#LG, Turtle Race
import turtle as t
import random

t.penup()
t.goto(600, 300)

t.pendown()
t.goto(600, -300)
t.hideturtle()

turtle_green = t.Turtle()
turtle_blue = t.Turtle()
turtle_red = t.Turtle()
turtle_purple = t.Turtle()
turtle_orange = t.Turtle()

turtle_purple.color("purple")
turtle_purple.shape("turtle")

turtle_orange.color("orange")
turtle_orange.shape("turtle")

turtle_red.color("red")
turtle_red.shape("turtle")

turtle_green.color("green")
turtle_green.shape("turtle")

turtle_blue.color("blue")
turtle_blue.shape("turtle")

turtle_green.penup()
turtle_green.goto(0, 100)
turtle_green.pendown()

turtle_red.penup()
turtle_red.goto(0, -100)
turtle_red.pendown()

turtle_purple.penup()
turtle_purple.goto(0, 200)
turtle_purple.pendown()

turtle_orange.penup()
turtle_orange.goto(0, -200)
turtle_orange.pendown()

all_turtles = [turtle_green, turtle_blue, turtle_red, turtle_purple, turtle_orange]

while True:
    chosen_turtle = random.choice(all_turtles)
    chosen_turtle.forward(50)
    if chosen_turtle.xcor() >= 600:
        print((chosen_turtle), "wins!")
        break
    


    
