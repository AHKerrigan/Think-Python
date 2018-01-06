""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-6:
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are okay). How many abecedarian words
are there?
"""

def is_abecedarian(word):
	"""Recieves a word as input and returns true if the letters in
	the word are in alphabetical order"""

	for i in range(len(word) - 1):
		print(i)
		if word[i] > word[i + 1]:
			return False
	return True

print(is_abecedarian('abcdef'))
print(is_abecedarian('abdxc'))

