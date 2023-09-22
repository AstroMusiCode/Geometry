import turtle
import math

t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(5)
def polygon(length, numSides):
    t.pendown()
    for i in range(numSides):
        t.forward(length)
        t.left(360 / numSides)
    t.penup()

# n1 and n2 are the two side lengths and dir is if each side
# length turns left or right (-1 or 1)
def rect(n1, n2, dir):
    t.pendown()
    for i in range(4):
        if (i%2 == 0):
            t.forward(n1)
        else:
            t.forward(n2)
        t.right(dir * 90)

def circle(radius):
        t.penup()
        t.circle(radius, 180)
        t.pendown()
        t.circle(radius)
        t.penup()

def ellipse(semiMajor, semiMinor, numSegments):
    t.penup()
    angleIncrement = 360 / numSegments
    
    # Calculate the starting point of the ellipse
    x_start = semiMajor * math.cos(math.radians(0))
    y_start = -semiMinor  # Start from the bottom
    
    t.setposition(x_start, y_start)
    t.pendown()
    
    for i in range(numSegments):
        x = semiMajor * math.cos(math.radians(i * angleIncrement))
        y = semiMinor * math.sin(math.radians(i * angleIncrement))
        t.setposition(x, y)
    
    t.penup()

ellipse(50, 100, 30)
ellipse(100, 50, 30)
circle(50)
polygon(50, 4)

input()