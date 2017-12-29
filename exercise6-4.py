""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 6-4:
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a
power of b."""

def is_power(a, b):
	"""Takes two values a and b and determines if a is a power of b
	"""

	# The base case is b being the first pwower of a, or that they equak
	if a == b:
		return True
	if a % b == 0 and is_power(a / b, b):
		return True
	else:
		return False

print(is_power(16,4))
print(is_power(24,4))
print(is_power(25,4))