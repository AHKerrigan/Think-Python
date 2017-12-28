""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 5-3: Write a program that takes the lengths of three lines and
determines if they could form a legitmate triangle.

Note: If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)
"""

def is_triangle(a, b, c):
	"""Takes the lengths of three lines, a, b, and c, and determines if they
	can form a triangle."""
	if (a > (b + c) or b > (a + c) or c > (a + b)):
		print("No")
	else:
		print("Yes")

def input_triangle():
	"""Prompts the user for 3 triangle lengths, then outputs if they
	form a legal triangle"""
	a = int(input('Enter the first length.\n'))
	b = int(input('Enter the second length.\n'))
	c = int(input('Enter the third length. \n'))
	is_triangle(a, b, c)

input_triangle()

