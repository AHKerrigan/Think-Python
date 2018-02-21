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


bob = turtle.Turtle()
flower(bob, 100.0, 7, 100.0)