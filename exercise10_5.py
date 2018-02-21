""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-5:
Write a function called is_sorted that takes a list as a parameter and returns True if
the list is sorted in ascending order and False otherwise.
"""

def is_sorted(t):
	"""Takes a list and returns  true if the list is 
	sorted in ascended order, false otherwise"""

	return t == sorted(t)

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))