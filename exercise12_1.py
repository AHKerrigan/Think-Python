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

def histogram(s):
	"""Takes a string as input and converts each letter to a key,
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

def swap_tuple_list(l):
	"""Takes a list of index size 2 tuples and returns a list with the elements of 
	each tuple swapped

	Keyword Arguments:
	l: The list of tuples taken as input

	Return Arguments
	swapped_list: The swapped list
	"""

	swapped_list = []

	for x, y in l:
		swapped_list.append((y, x))
	return swapped_list


def most_frequent(phrase):
	"""Takes a string as input and prints the letters in
	decreasing order of frequency"""

	# Converst the string into a sorted list of tuples, containing each
	# letter and their frequency
	listed_histogram = dictionary_to_tuple_list(histogram(phrase))

	# Swaps that list the sorts it
	# Could be done without swapping with an additional package, but 
	# We will stick with the book
	listed_histogram = sorted(swap_tuple_list(listed_histogram), reverse=True)

	for frequency, letter in listed_histogram:
		print(letter, frequency)


most_frequent("There are three ways to count letter frequency that result in very different charts for common letters. The first method, used in the chart below, is to count letter frequency in root words of a dictionary. The second is to include all word variants when counting, such as abstracts, abstracted and abstracting and not just the root word of abstract. This system results in letters like s appearing much more frequently, such as when counting letters from lists of the most used English words on the Internet. A final variant is to count letters based on their frequency of use in actual texts, resulting in certain letter combinations like th becoming more common due to the frequent use of common words like the. Absolute usage frequency measures like this are used when creating keyboard layouts or letter frequencies in old fashioned printing presses.")