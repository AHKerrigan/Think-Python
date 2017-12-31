""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 7-3:
Write a function called estimate_pi that uses this [Ramanujan's] formula to compute and return an
estimate of π. It should use a while loop to compute terms of the summation until the 
last term is smaller than 1e-15 (which is Python notation for 10−15). You can check
the result by comparing it to math.pi.
"""

import math

def estimate_pi():
	"""Estimates pi using Ramanujan's formula to an error of less than 1e-15
	"""

	within_epsilon = False # Sentinal variable for the requisit error.
	epsilon = 1e-15
	sigma = 0.0 # The infinite series will be its own value, for simplicity
	constant = (2 * math.sqrt(2)) / 9801 # The constant that multiplies sigma
	comparison = 1 / math.pi # Ramanujan's formula yields the inverse of pi so we compare against that
	k = 0 # A while loop works better here, so this will be used to count the infinite series 

	while not within_epsilon:
		sigma = sigma + ((math.factorial(4*k) * (1103 + 26390 * k))) / ((math.factorial(k)**4) * (396**(4 * k)))
		within_epsilon = abs(comparison - (sigma * constant)) < epsilon
		k = k + 1

	print(k)
	return 1 / (constant * sigma)


print(estimate_pi())
