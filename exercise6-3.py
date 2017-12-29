""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 6-3:
Write a function that tests if a given string is a palindrome

NOTE: the first, last, and middle functions were given for this
particular exercise."""

def first(word):
	"""takes a string and returns the first letter
	"""
	return word[0]

def last(word):
	"""takes a string and returns the last letter
	"""
	return word[-1]

def middle(word):
	"""Takes a string and returns the text between the 
	first and last letter"""
	return word[1:-1]

def is_palindrome(word):
	"""takes a string and determines if it is a palindrome
	"""
	# The degenerate case is 1 letter or none. We consider these palindromes
	if len(word) <= 1:
		return True

	# For something to be a palindrome, the first and last letters much match
	# and the string between them must also be a palindrome
	if first(word) == last(word) and is_palindrome(middle(word)):
		return True
	else:
		return False



print(is_palindrome("kerrigan"))
print(is_palindrome("kayak"))