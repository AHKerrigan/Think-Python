"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/


This program will draw a Archimedian spiral
"""

import turtle

def spiral(t, a, b, n, length):
	"""draws a spiral with n line segments length long. A denotes the radius of the initial spiral
	b denotes the looseness of the entire spiral"""
	theta = 0.0

	for i in range(n):
		t.fd(length)
		dtheta = 1 / (a + b * theta)
		t.lt(dtheta)
		theta += dtheta

bob = turtle.Turtle()

# Both a and b need to be quite small or the spiral goes off screen

spiral(bob, 0.01, 0.0002, 50, 3)
turtle.mainloop()
