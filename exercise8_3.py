""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 8-3:
Use string splices to rewrite is_palindrome using one line
"""

def is_palindrome(phrase):
	"""Takes a string as input and returns whether that
	string is a palindrome or not"""

	return phrase[::-1] == phrase

print(is_palindrome('Kerrigan'))
print(is_palindrome('kayak'))