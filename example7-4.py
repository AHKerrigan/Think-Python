""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 7 Example 4:

Encapsulate and generalize the count function"""

def count(word, character):
	"""Takes a word and a letter and output the number of
	times that letter appears in the word"""
	count = 0
	for letter in word:
		if letter == character:
			count = count + 1
	return count

print(count('banana', 'a'))