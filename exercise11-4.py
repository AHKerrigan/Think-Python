""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 11-4:
If you did Exercise 10-7, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more
than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates ."""

def has_duplicates(t):
	"""Takes a list as input and returns true if that list contains
	any duplicates

	Keyword Arguments:
	t: list we are checking"""

	hashed_list = dict()

	# Holds a memo of the list. If at any point an item has
	# already been written in the memo, we return True
	for item in t:
		if item in hashed_list:
			return True
		else:
			hashed_list[item] = ''
	return False

print(has_duplicates([1,2,3,4,5,4,3,5,6,7,8,9]))
print(has_duplicates([1,2,3,4,5,6,7,8,9,19]))


