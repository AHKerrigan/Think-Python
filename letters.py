import math
import turtle


""" From Exercise 4-4 from Think Python
The letters of the alphabet can be constructed from a moderate number of basic elements,
like vertical and horizontal lines and a few curves. Design an alphabet that can
be drawn with a minimal number of basic elements and then write functions that
draw the letters. This uses the turtle function"""

# Primatives 
def fdbk(t, n):
	"""Draws a line of length n then returns 
	"""
	t.fd(n)
	t.lt(180)
	t.fd(n)

def fdbkhalf(t,n):
	"""Draws a line of length n then returns halfway
	"""
	t.fd(n)
	t.lt(180)
	t.fd(n / 2)

# GEOMETRIC FUNCTIONS

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


def hypotenuse(x, y):
	return (x**2 + y**2)**(1/2)



# Letters
# All letters are upper case and n units high

def draw_a(t, n):
	beam_length = hypotenuse(n, n / 2)
	beam_angle = 90 - math.degrees(math.atan(1/2))
	cross_length = n - (math.cos(math.radians(beam_angle)) * beam_length)
	t.lt(beam_angle)
	t.fd(beam_length)
	t.rt(beam_angle * 2)
	fdbkhalf(t, beam_length)
	t.lt(beam_angle)
	fdbk(t, cross_length)
	t.rt(beam_angle)
	t.fd(beam_length / 2)
	t.lt(beam_angle)



"""	
TODO 

def draw_b()
def draw_c()
def draw_d()
def draw_e()
def draw_f()
def draw_g()
def draw_h()
def draw_i()
def draw_j()
def draw_k()
def draw_l()
def draw_m()
def draw_n()
def draw_o(t, n)
	circle(t, n / 2)
def draw_p()
def draw_q()
def draw_r()
def draw_s()
def draw_t()
def draw_u()
def draw_v()
def draw_w()
def draw_x()
def draw_y()
def draw_z()
"""



bob = turtle.Turtle()
draw_a(bob, 300)
turtle.mainloop()