#LG, Turtle Race
import turtle as t
import random

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

turtle_green.forward(600)
turtle_blue.forward(600)
turtle_red.forward(600)
turtle_purple.forward(600)
turtle_orange.forward(600)



