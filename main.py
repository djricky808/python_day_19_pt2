from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

root = screen.getcanvas().winfo_toplevel()
root.call('wm', 'attributes', '.', '-topmost', '1')

colors = ['red','orange', 'yellow', 'green', 'blue', 'purple', 'grey']
all_turtles = []

for t in range(len(colors)):
    new_turtle = Turtle(shape = "turtle" )
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + 33 * t)

screen.exitonclick()