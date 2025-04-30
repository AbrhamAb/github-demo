from turtle import Screen
from turtledemo.clock import setup
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import random
from scoreboard import ScoreBoard

screen= Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
difficulty = screen.textinput("Difficulty", "Choose difficulty: Easy / Medium / Hard").lower()

# Set game speed based on difficulty
if difficulty == "easy":
    speed = 0.2
elif difficulty == "medium":
    speed = 0.1
else:  # hard or anything else
    speed = 0.05

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.listen()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
#we should detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # Step 2: Change background color after score 10
        if scoreboard.score > 5:
            screen.bgcolor("blue")
#DETECT COLLISION WITH WALL
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
#detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()