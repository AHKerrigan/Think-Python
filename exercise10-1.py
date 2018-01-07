""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-1:
Write a function called nested_sum that takes a list of lists of integers and adds up the
elements from all of the nested lists.
"""

def nested_sum(L):
	"""Takes a list of integer lists and finds the total sum
	of all its elements"""

	total = 0

	# It seems rereading the problem, the nests only go one deep
	for x in L:
		for y in x:
			total += y
	return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

