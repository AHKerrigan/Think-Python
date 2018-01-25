""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 11-2
Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict .
"""

def invert_dict(d):
	"""Takes a dictionary as input and outputs that dictionary
	inverted

	Keyword Arguments:
	d: The input dictionary

	Return Arguments:
	Inverse: The inverse of the dictionary"""

	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)

	return inverse


print(invert_dict({'a' : 1, 'p' : 1, 'r': 2}))