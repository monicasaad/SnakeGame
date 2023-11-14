# import required modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# create screen object from Screen class
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# turn off tracer
screen.tracer(0)
screen.title("Snake Game")

# create snake object from Snake class
snake = Snake()
# create food object from Food class
food = Food()
# create scoreboard object from Scoreboard class
scoreboard = Scoreboard()

# set screen to listen for events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# variable to check if game is on
is_game_on = True
# keep moving while game is on
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 19:
        scoreboard.increase_score()
        snake.add_segment()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        # is_game_on = False
        scoreboard.reset_score()
        snake.reset_snake()

    # detect collision with tail
    for segment in range(len(snake.all_segments) - 1, 1, -1):
        if snake.head.distance(snake.all_segments[segment]) < 10:
            # scoreboard.game_over()
            # is_game_on = False
            scoreboard.reset_score()
            snake.reset_snake()

# keep screen popup open
screen.exitonclick()
