import turtle
from random import randint
from turtle import Turtle
screen = turtle.Screen()
screen.setup(width=500,height=400)
listOfTurtles = []
numOfTurtles = 7
setOfcolors= ['Red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
userBet=(screen.textinput("Make your BETS!","Which color turtle will win the Race? Enter a color"))
turtlex = turtle.Turtle()
turtlex.penup()
turtlex.goto(0,0)
turtlex.pendown()
turtlex.hideturtle()
for i in range(numOfTurtles):
    listOfTurtles.append(turtle.Turtle())
    Turtle = listOfTurtles[i]
    Turtle.penup()
    Turtle.shape("turtle")
    listOfTurtles[i].color(setOfcolors[i])
    Turtle.goto(x=-235,y=50*(i)-150 )
def victory(turtleList,width):
    for turtle in turtleList:
        xpos = turtle.pos()
        if xpos[0] >=(width/2)-28:
            return turtle.color()[0]
        else:
            continue
        return

while victory(listOfTurtles,500)==None:
    for turtle in listOfTurtles:
        turtle.forward(randint(0,80))
winner = (victory(listOfTurtles,500))
if winner.title()==userBet.title():
    output=("You win!")
else:
    output=(f"You lose\n{winner.title()} Won")

style = ('Courier', 30, 'italic')
turtlex.write(output,font=style,align='center')






screen.exitonclick()
