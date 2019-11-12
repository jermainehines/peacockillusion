import turtle

bob=turtle.Turtle()
turtle.colormode(255)

def square (distance):
    for times in range (4):
        bob.forward (distance)
        bob.left (90)

def polygon(sides,distance, c):
    bob.color(c)
    angle=360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def triangle(distance):
    for times in range (3):
        bob.forward(distance)
        bob.left (120)

def pentagon (distance):
    sides=5
    angle=360/sides
    for times in range (sides):
        bob.forward (distance)
        bob.left (angle)



def jump (x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()


def fadingTriangle():
    for times in range(50):
        c=(250-times*5,250-times*5,0)
        polygon(3,450 - times*8,c)

def tile():
  for times in range (4):
    polygon (3,100,"black")
    bob.forward (50)
    polygon (3,100,"black")
    bob.forward (50)
    polygon (3,100,"black")
    bob.forward (50)
    polygon (3,100,"black")
    bob.forward(50)
    bob.left (90)

def spikeFlower(distance):
    for times in range(90):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*36)
        
def spike(distance):
    for times in range(20):
        c=times*12
        bob.color(c,c,c)
        bob.width(times*1.5)
        bob.forward(distance)
        bob.left(5)
        bob.circle(50)
        bob.forward(100)
