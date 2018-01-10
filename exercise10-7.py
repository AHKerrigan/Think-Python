""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-7:
Write a function called has_duplicates that takes a list and returns True if there is
any element that appears more than once. It should not modify the original list."""

def has_duplicates(t):
	"""Takes a list as input and returns true if that list contains
	any duplicates"""

	# Each element will check each following elements for its duplicate
	# An element looking for duplicates before itself is redundant
	for i in range(len(t)):
		for n in t[i + 1:]:
			if t[i] == n:
				return True
	return False

print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 3, 1, 4, 5]))