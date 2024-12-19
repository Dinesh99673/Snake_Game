from turtle import Screen
import time
import snake
import food
import scoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreBoard = scoreBoard.ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increase()
        snake.extend()

    #Detect Collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreBoard.gameOver()

    #Detect collision with tail (considering whole pat other than head as tail)
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 5:
            game_is_on = False
            scoreBoard.gameOver()


    

screen.exitonclick()