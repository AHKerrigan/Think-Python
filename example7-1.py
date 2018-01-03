""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 7 Example 1:

As an exercise, write a function that takes a string as an argument and displays the
letters backward, one per line.
"""

def print_backwards(phrase):
	"""Takes a string as input and prints it backwards line by line
	"""
	index = len(phrase) - 1
	while index >= 0:
		print(phrase[index])
		index = index - 1

print_backwards("Kerrigan") 