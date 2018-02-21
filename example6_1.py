""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 6 Example 1:

As an exercise, write a compare function takes two values, x and y, and returns 1 if x
> y, 0 if x == y, and -1 if x < y.
"""
def compare(x, y):
	"""Takes two values x and y. Returns 1 if x > y, 0 if x ==y,
	and - 1 if x < y"""
	if x > y:
		return 1
	if  x == y:
		return 0
	else:
		return -1
print(compare(4 , 5))
	