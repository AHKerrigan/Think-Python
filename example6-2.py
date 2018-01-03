""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 6 Example 2:

As an exercise, use incremental development to write a function called hypotenuse
that returns the length of the hypotenuse of a right triangle given the lengths of the
other two legs as arguments. Record each stage of the development process as you go.
"""

import math

def hypotenuse(x, y):
	"""Takes the triangle side lengths x and y and compust their
	hypotenuse"""
	x_sqr = x**2
	y_sqr = y**2
	tri_sqr = x_sqr + y_sqr
	return math.sqrt(tri_sqr)

print(hypotenuse(3, 4))