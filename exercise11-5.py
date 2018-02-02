""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 11-5: 
Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_word in Exercise 8-5).

Write a program that reads a wordlist and finds all the rotate pairs.
"""



def rotate_word(phrase, count):
	"""Takes a phrase and an integer as inputs, then rotates the 
	string Ceasar cypher styles by the number of places given"""

	new_phrase = '' 

	# Variable for holding the new numeric value of each character after the cypher
	place_new = 0

	for c in phrase:
 
		place_new = ord(c) + count
		 
		# These statements are for looping the character back around the alphabet if it goes out of bounds
		# Uppercase goes from 65 to 90, Lowercase from 97 to 122
		# We start one off (example 64 instead of 65 for A) so "+1" goes to A from Z
		if c.isupper():
			while place_new > 90:
				place_new = 64 + (place_new - 90)
			while place_new < 65:
				place_new = 91 - (65 - place_new)
		if c.islower():
			while place_new > 122:
				place_new = 96 + (place_new - 122)
			while place_new < 97:
				place_new = 123 - (97 - place_new)

		new_phrase = new_phrase + chr(place_new)

	return new_phrase



def print_rotate_pairs(file):
	"""Takes a wordlist filename as input and prints all rotate pairs in te
	word list

	Keyword Arguments: 
	file: a string that represents a filename"""

	fin = open(file)
	checked_words = dict()


	for item in fin:
		if item in checked_words:
			continue
		