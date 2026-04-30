from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

valid_bet_placed = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

root = screen.getcanvas().winfo_toplevel()
root.call('wm', 'attributes', '.', '-topmost', '1')

colors = ['red','orange', 'yellow', 'green', 'blue', 'purple', 'grey']
all_turtles = []

while not valid_bet_placed:
    if user_bet in colors:
        valid_bet_placed = True
    else:
        user_bet = screen.textinput(title="Make your bet", prompt=f"Invalid color. Please use :{colors} ")


for t in range(len(colors)):
    new_turtle = Turtle(shape = "turtle" )
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + 33 * t)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()