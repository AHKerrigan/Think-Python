import math
import turtle

def polyline(t, n, length, angle):
	"""Draws n line segments with the given length and
	angle (in degrees) between them. t is a turtle.
	"""
	for i in range(n):
		t.fd(length)
		t.lt(angle)

def polygon(t, length, n):
	"""Draws an Ngon made up of equal angles of the given length
	t is a turtle
	"""
	angle = (360 / n)
	polyline(t, n, length, angle)

def arc(t, r, angle):
	"""Draws a arc, or piece of a circle, of an angle and given radium
	"""

	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 4) + 3
	step_length = arc_length / n
	step_angle = float(angle) / n

	# making a slight left turn before starting reduces the 
	# error of linear approximation of the arc

	t.lt(step_angle/2)
	polyline(t, n, step_length, step_angle)
	t.rt(step_angle/2)

def circle(t, r):
	arc(t, r, 360)

def petal(t, r, angle):
	for i in range(2):
		arc(t, r, angle)
		t.lt(180-angle)

def flower(t, r, n, angle):
	"""Draws a flower with n petals, with petal length r, sepended by an angle
	"""
	for i in range(n):
		petal(t, r, angle)
		t.lt(360.0 / n)

def spoke_length(n, length):
	"""Uses some simple trig and algebra to determine the length of the inner
	spokes of a polygon given n sides and the side length"""

	interior_angle = (2 * math.pi) / n #finds the interior angle in radians
	return ((length**2) / (2 * (1 - math.cos(interior_angle))))**(1/2)

def polyspokes(t, n, length):
	"""Draws the inner spokes of a polygon given a turtle, a length, and an n
	"""
	line_length = spoke_length(n, length)

	for i in range(n):

		# Draws a line then turns back around
		polyline(t, 2, line_length, 180)
		t.lt(360 / n)

def spoked_polygon(t, n, length):
	"""Takes a number of sides and side lengths and outputs a polygone
	containing spokes leading to the center. t is a turtle"""

	polyspokes(t, n, length)

	# polyspokes leaves us in the middle so we have to travel outside to begin the polygon
	t.fd(spoke_length(n, length))
	t.lt(90 + 180 / n)
	polygon(t, length, n)

bob = turtle.Turtle()
spoked_polygon(bob, 10, 150)
turtle.mainloop()