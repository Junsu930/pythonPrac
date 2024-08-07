from turtle import Turtle, Screen
import random
from tkinter import messagebox

is_race_on = False
winner = ""
screen = Screen()
screen.setup(500, 400)
colors = ["red", "blue", "orange", "purple", "black"]
y_points = [60, 30, 0, -30, -60]
turtles = ["red", "blue", "orange", "purple", "black"]

while True:
    userChoice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
    if colors.__contains__(userChoice):
        break

for i in range(0, 5):
    turtles[i] = Turtle()
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-240, y_points[i])

while True:
    chosenTurtle = random.randint(0, 4)
    turtles[chosenTurtle].forward(2)
    if turtles[chosenTurtle].xcor() > 250:
        winner = colors[chosenTurtle]
        break

if winner == userChoice:
    messagebox.showinfo("축하",f"축하합니다! {winner} 우승! 배팅 성공!")
else :
    messagebox.showinfo("실패",f"{winner} 우승! 배팅 실패!")

screen.exitonclick()
