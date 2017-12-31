""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 7-1:
Implement Newton's Method for finding square roots using iteration."""

import math

def mysqrt(a):
	"""Takes a value a and uses Newton's Method to find a estimate for the 
	square root"""

	# For all a 2 or greater, the square root can be no more than half of a
	# so its a good place to start estimating
	x = a/2 

	while True:
		y = (x + a/x) / 2
		if y == x:
			break
		x = y

	return y

def test_square_root():
	"""Prints a table that states the Newton's Method estimate as well as
	the true value of the square root of the integers 1 through 9. At the end
	the table prints the difference between the estimate and the true value
	"""

	print("a", " "*3, "mysqrt(a)", " "*9, "math.sqrt(a)", " "*7, "diff")
	print("-", " "*3, "-"*9, " "*9, "-"*12, " "*7, "-"*4)

	for i in range(1, 10):

		# We compute the values first to save outselves a calcuation 
		estimate = mysqrt(float(i))
		true = math.sqrt(float(i))
		diff = abs(estimate - true)

		# I seperate the perfect squares so that we can have the right number of spaces
		# for the table and not have to have a print statement for every line.
		if i in {1, 4, 9}:
			print(float(i), " ", estimate, " "*15, true, " "*15, diff)
		else:
			print(float(i), " ", estimate, " "*1, true, " "*1, diff)

test_square_root()