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

def rotate_pairs(word, word_dict):
	""" Takes a word and a word dictionary, then prints out every words that exist
	in the word dictionary that rae a rotate pair with that word
	"""

	# Holds the current word being looked for so we don't have to rotate twice
	current_word = ''

	for i in range(1, 21):
		current_word = rotate_word(word, i)
		if current_word in word_dict:
			print(word, " ", current_word)


def file_to_dict(fin): 
	"""Takes a file as input and returns  a dictionary version of that file
	"""

	dicted_file = dict()
	for line in fin:
		dicted_file[line.strip()] = ''
	return dicted_file


def find_rotate_pairs(wordlist):
	"""Takes a wordlist filename as input and prints all rotate pairs in thbe
	word list

	Keyword Arguments:
	file: The file we will be printing rotate pairs from
	"""

	word_dictionary = file_to_dict(open(wordlist))

	for item in word_dictionary:
		rotate_pairs(item, word_dictionary)

find_rotate_pairs("words.txt")
