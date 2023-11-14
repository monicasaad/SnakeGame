# import required modules
from turtle import Turtle

# define constants
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# define a class called Snake
class Snake:
    def __init__(self):
        # list to hold all segment objects
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        x_cord = 0
        for snake_seg in range(0, 3):
            # create new turtle object
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            # adjust starting position of segment
            new_segment.goto(x_cord, 0)
            # decrease value of x_cord so segment created in following iteration moves behind existing segments
            x_cord -= 20
            # add new_segment object to all_segments list
            self.all_segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.all_segments[-1].position())
        self.all_segments.append(new_segment)

    def move(self):
        # range(start, stop, step)
        for segment in range(len(self.all_segments) - 1, 0, -1):
            # new position of current segment is set to position of segment ahead of it
            new_x = self.all_segments[segment - 1].xcor()
            new_y = self.all_segments[segment - 1].ycor()
            # move segment to new position
            self.all_segments[segment].goto(new_x, new_y)
        # move first segment forwards and with loop, the rest will follow
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for seg in self.all_segments:
            seg.hideturtle()
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]
