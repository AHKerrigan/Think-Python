""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 12 Example 1:

As an exercise, write a function called sumall that takes any number of arguments
and returns their sum."""

def sumall(*values):
	"""Takes a number of values as input and returns their sum
	"""
	# The final sum that we will return
	total = 0

	for i in values:
		total += i

	return total 

print(sumall(1, 2, 3, 4, 5, 6, 7, 8, 9))