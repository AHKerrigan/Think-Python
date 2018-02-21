""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 7 Example 3:

As an exercise, modify find so that it has a third parameter: the index in word where
it should start looking."""

def find(word, letter, start):
	"""Takes a word, a letter, and a starting point, and finds the index
	where the letter is located in the word"""
	index = start
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return - 1
