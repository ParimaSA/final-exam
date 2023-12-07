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
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_all(num_p, num_side, multiply):
    if multiply:
        for i in range(num_p):
            p = Polygon(num_side)
            p.draw_inside()
    else:
        for i in range(num_p):
            p = Polygon(num_side)
            p.draw_polygon()


class Draw_Art:
    def __init__(self, num_pic = 30, random = False, inside = False, num_side = 3):
        self.num_pic = num_pic
        self.random = random
        self.inside = inside
        self.num_side = num_side

    def draw(self):
        if self.random:
            self.draw_random_side()
        else:
            self.draw_simple_side()

    def draw_random_side(self):
        for _ in range(self.num_pic):
            num_side = random.randint(3, 5)
            p = Polygon(num_side)
            if self.inside:
                p.draw_inside()
            else:
                p.draw_polygon()

    def draw_simple_side(self):
        for _ in range(self.num_pic):
            p = Polygon(self.num_side)
            if self.inside:
                p.draw_inside()
            else:
                p.draw_polygon()


num_pic = random.randint(20,40)
all_pic = Draw_Art(num_pic)

choice = input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: ')
if choice not in [str(x) for x in range(1, 9)]:
    choice = input('Which art do you want to generate? Enter a number between 1 to 8,inclusive: ')

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# customize the polygon to be the following art
if choice == '1':
    pass  # original one triangle with no polygon inside
elif choice == '2':
    all_pic.num_side = 4  # change side to 4
elif choice == '3':
    all_pic.num_side = 5  # change side to 5
elif choice == '4':
    all_pic.random = True  # change to be random side
elif choice == '5':
    all_pic.inside = True  # triangle but to polygon inside
elif choice == '6':
    all_pic.inside = True  # polygon inside
    all_pic.num_side = 4   # change side to 4
elif choice == '7':
    all_pic.inside = True  # polygon inside
    all_pic.num_side = 5   # change side to 5
else:
    all_pic.inside = True  # polygon inside
    all_pic.random = True  # change to random side

all_pic.draw()  # draw pic after customize

turtle.done()