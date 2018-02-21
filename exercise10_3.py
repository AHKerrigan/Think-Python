""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-3:
Write a function called middle that takes a list and returns a new list that contains all
but the first and last elements.
"""

def middle(t):
	"""Takes a list as input and returns all but the first and
	last elements"""
	return t[1:-1]

t = [1, 2, 3, 4]
print(middle(t))