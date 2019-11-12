import turtle

bob=turtle.Turtle()
turtle.colormode (255)



def spikeFlower1(distance):
    for times in range (50):
        spike1(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.right(times*20)

def spike1(distance):
    for times in range(20):
        c=times*10
        bob.color(c,c,c)
        bob.width(times*1)
        bob.forward(distance)
        bob.left(8)
        bob.circle(times*2.5)
        bob.forward(20)

def spikeFlower(distance):
    for times in range (90):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times*35)


def spike(distance):
    for times in range(20):
        c=times*12
        bob.color(60,c,135)
        bob.width(times*1.8)
        bob.forward(distance)
        bob.left(9)
        bob.circle(25)
        bob.forward(40)

