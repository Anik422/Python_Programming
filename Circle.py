import turtle

turtle.bgcolor('black')
turtle.pen(2)
turtle.speed(10)
for i in range(500):
    if i%2==0:
        for color in ["white", "cyan", "blue", "yellow", "red", "green"]:
            turtle.color(color)
            turtle.circle(150)
            turtle.left(10)
    elif i%2!=0:
        for color in ["white", "cyan", "blue", "yellow", "red", "green"]:
            turtle.color(color)
            turtle.circle(150)
            turtle.right(5)
    # else:
    #     for color in ["white", "cyan", "blue", "yellow", "red", "green"]:
    #         turtle.color(color)
    #         turtle.circle(150)
    #         turtle.right(5)
# for i in range(10):
#     turtle.speed(10)
#     turtle.shapesize(1, 5, 10)
#     turtle.shapesize(10, 5, 1)
#     turtle.shapesize(1, 10, 5)
#     turtle.shapesize(10, 1, 5)

turtle.hideturtle()