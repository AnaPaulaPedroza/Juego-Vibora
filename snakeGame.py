from turtle import *
from random import choice, randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors_list = ['magenta', 'yellow', 'aquamarine', 'purple', 'pink']
colorSnake = choice(colors_list)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    global colorSnake, food
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        colorSnake = colorFood
        colorFood = choice(colors_list)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, "black")

    square(food.x, food.y, 9, colors[colorFood])
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
bgcolor('#F8F8FF')
hideturtle()
tracer(False)
listen()
colors = ["black", "green", "blue", "yellow", "#FFA501"]
colorFood = randrange(0,4)
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()