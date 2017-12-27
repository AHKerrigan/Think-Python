import turtle
import math

# Book verison of the sqaure
# Takes a turtle and then a length for the square
"""Adding a parameter to a function is called generalization because it makes the function
more general: in the previous version, the square is always the same size; in this
version it can be any size."""
def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)


#Polygon is a general form of the square, it takes a n and draws a n gone with length sides given

def polygon(t, n, length):
	angle = 360 / n
	for i in range(n):
		t.fd(length)
		t.lt(angle)



bob = turtle.Turtle()

# Calling the square
square(bob, 100)

""
polygon(bob, n=7, length=70)
turtle.mainloop()