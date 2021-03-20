

import turtle
import time
import random



delay = 0.1








wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width= 600, height = 600)
wn.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape ("square")
head.color ("white")
head.penup()
head.goto(0,0)
head.direction = "stop"



#food

food = turtle.Turtle()
food.speed(0)
food.shape ("square")
food.color ("red")
food.penup()
food.goto(0,100)

segments = []

# pen
#pen = turtle.Turtle()
#pen.speed(0)
#pen.shape("square")
#pen.color("white")
#pen.penup()
#pen.hideturtle()
#pen.goto(0, 260)




#functions


def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# key board bindings

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



#game loop

while True:
    wn.update()

    #check for collisions (wall)
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"


        #hide segments
        for segment in segments:
            segment.goto (1000,1000)


            # clear the segments list
        segments.clear()









    # check for collision
    if head.distance(food) < 20:
        #move food random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)











    #move end segments

    for index in range (len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)



    #move segments 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()



    # body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


            #hide segments again
            for segment in segments:
                segment.goto(1000, 1000)


            # clear the segments list
            segments.clear()




    time.sleep(delay)

wn.mainloop()