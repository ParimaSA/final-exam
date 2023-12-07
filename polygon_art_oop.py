import turtle
import random


class Polygon:
    def __init__(self, num_side):
        self.num_sides = num_side # triangle, square, or pentagon
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def draw_inside(self):
        self.draw_polygon()
        for i in range(2):
            reduction_ratio = 0.618
            turtle.penup()
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= reduction_ratio
            self.draw_polygon()

    @staticmethod
    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_all(num_p, num_side, multiply):
    if multiply:
        for i in range(num_p):
            p = Polygon(num_side)
            p.draw_inside()
    else:
        for i in range(num_p):
            p = Polygon(num_side)
            p.draw_polygon()


num_pic = random.randint(20,40)
choice = input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: ')
if choice not in [str(x) for x in range(1,9)]:
    choice = input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: ')
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
if choice == '1':
    draw_all(num_pic, 3, False)
elif choice == '2':
    draw_all(num_pic, 4, False)
elif choice == '3':
    draw_all(num_pic, 5, False)
elif choice == '4':
    for i in range(num_pic):
        num_s = random.randint(3,5)
        p = Polygon(num_s)
        p.draw_polygon()
elif choice == '5':
    draw_all(num_pic, 3, True)
elif choice == '6':
    draw_all(num_pic, 4, True)
elif choice == '7':
    draw_all(num_pic, 5, True)
else:
    for i in range(num_pic):
        num_s = random.randint(3, 5)
        p = Polygon(num_s)
        p.draw_inside()

turtle.done()