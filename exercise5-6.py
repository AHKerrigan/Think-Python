""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 5-6: 
1: Write a function called koch that takes a turtle and a length as parameterse, and that
uses the turtle to draw a Koch curve with the given legnth

2: Write a function called snowflake that draws three Koch curves to make the out-line
of a snowflake

3: Generalized. Here, I generalized it by allowing a snowflake/curve of any order
n to be drawn. The higher the order, the deeper the fractal.

"""

import turtle

def koch(t, x, n):
	"""Draws a koch curve of length x and order n
	"""
	if n == 0:
		t.fd(x)
		return
	koch(t, x / 3, n - 1)
	t.lt(60)
	koch(t, x / 3, n - 1)
	t.rt(120)
	koch(t, x / 3, n - 1)
	t.lt(60)
	koch(t, x / 3, n - 1)

def snowflake(t, x, n):
	"""Draws a snowflake with size x using koch curves of order n
	"""
	for i in range(3):
		koch(t, x, n)
		t.rt(120)


bob = turtle.Turtle()
snowflake(bob, 60, )
turtle.mainloop()