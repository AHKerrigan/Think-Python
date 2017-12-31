""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 5-5:
This exercise is simply a copy-paste to determine if the reader
understands what is being done. It is a fractal of order n.
"""

import turtle 

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.fd(length*n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2*angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length*n)

bob = turtle.Turtle()
draw(bob, 20, 5)