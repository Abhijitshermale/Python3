from turtle import Turtle

MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self,):
        super(Player, self).__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.go_to_start()

    def moveUp(self):
        y_move = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),y_move)

    def moveDown(self):
        y_move = self.ycor()-MOVE_DISTANCE
        self.goto(self.xcor(), y_move)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        pass

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



