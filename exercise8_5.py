""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 8-5:
Write a function called rotate_word that takes a string and an integer as parameters,
and returns a new string that contains the letters from the original string rotated by
the given amount.
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


print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
print(rotate_word('IBM', -1))
print(rotate_word('zzzZZZ', 1))
