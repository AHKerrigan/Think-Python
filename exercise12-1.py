""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 12-1: 
Write a function called most_frequent that takes a string and prints the letters in
decreasing order of frequency. Find text samples from several different languages and
see how letter frequency varies between languages. Compare your results with the
tables at http://en.wikipedia.org/wiki/Letter_frequencies.
"""

def historgram(s):
	"""Takes a strings as input and converts each letter to a key,
	with the value being the number of times that letter appears"""

	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

def dictionary_to_tuple_list(d):
	"""Takes a dictionary as input and returns a list of tuples
	containing the keys and values"""

	tuple_list = []
	for x, y in d.items():
		tuple_list.append((x, y))
	return tuple_list
def swa



def most_frequent(phrase):
	"""Takes a string as input and prints the letters in
	decreasing order of frequency"""

	# Converst the string into a sorted list of tuples, containing each
	# letter and their frequency
	listed_histogram = dictionary_to_tuple_list(historgram(phrase))
	

	for letter, frequency in listed_histogram:
		print(letter, frequency)

most_frequent("supercalifragilisticexpeialidocious")