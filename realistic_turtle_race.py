#LG, Turtle Race
import turtle as t
import random

t.exitonclick

t.penup()
t.goto(600, 300)

t.pendown()
t.goto(600, -300)
t.hideturtle()

turtle_green1 = t.Turtle()
turtle_green2 = t.Turtle()
turtle_green3 = t.Turtle()
turtle_green4 = t.Turtle()
turtle_green5 = t.Turtle()

turtle_green1.color("green")
turtle_green1.shape("turtle")

turtle_green2.color("green")
turtle_green2.shape("turtle")

turtle_green3.color("green")
turtle_green3.shape("turtle")

turtle_green4.color("green")
turtle_green4.shape("turtle")

turtle_green5.color("green")
turtle_green5.shape("turtle")

turtle_green1.penup()
turtle_green1.goto(0, 100)
turtle_green1.pendown()

turtle_green2.penup()
turtle_green2.goto(0, -100)
turtle_green2.pendown()

turtle_green3.penup()
turtle_green3.goto(0, 200)
turtle_green3.pendown()

turtle_green4.penup()
turtle_green4.goto(0, -200)
turtle_green4.pendown()

all_turtles = [turtle_green1, turtle_green2, turtle_green3, turtle_green4, turtle_green5]

while True:
    chosen_turtle = random.choice(all_turtles)
    winning_color = chosen_turtle.pencolor()
    chosen_turtle.forward(0.25)
    if random.random() < 0.1:
        turn_angle = random.choice([-15, 15])
        chosen_turtle.right(turn_angle)
    if chosen_turtle.xcor() >= 600:
        print(f"Turtle Wins!")
        break

t.done