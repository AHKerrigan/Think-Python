import turtle
import math 

# Takes a turtle t, and draws a square with lengths
def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

# Draws an n sided polygon of length given
def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

# Has the turtle t draw a circle of radius r
# Its an APPROXIMATE circle, so we basically make an 100gon
def circle(t, r):

	# we determine the length by using 2πr definition of circumference, and setting it equal to L*100, then algebra
	length = ((math.pi*r)/50)
	polygon(t, length, 100)

# General version of the circle that draws an angle sized arc of a circle
# We can't reuse polygon because its designed to turn back on itself
def arc(t, r, angle):

	# Some algebra to find arc length given radius and angle 
	arc_length = ((math.pi*r*angle)/180)

	# We make angle many 1 degree turns, and moveforward 1/angle of the arc length each time
	for i in range(angle):
		t.fd(arc_length/angle)
		t.lt(1)

bob = turtle.Turtle()


square(bob, 200) # draws a square
polygon(bob, 100, 8)
arc(bob, 50, 360)
arc(bob, 100, 170)

turtle.mainloop()
