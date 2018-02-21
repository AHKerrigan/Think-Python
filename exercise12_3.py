""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/


Exercise 12-3
Two words form a “metathesis pair” if you can transform one into the other by swap‐
ping two letters; for example, “converse” and “conserve”. Write a program that finds
all of the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and
don’t test all possible swaps.
"""


def tupled_string(phrase):
	"""Takes a string as input and returns a tuple with each
	letter as an element"""

	# The tuple to be returned
	ts = tuple()

	for element in phrase:
		ts = ts + (element,)

	return ts

def tuple_sort(t):
	"""Because by default sorting a tuple turns it into a list, this function
	takes a tuple as input, sorts it, turns it back into a tuple, then returns 
	that sorted tuple"""

	listed_t = sorted(t)
	return_t = tuple()

	for element in listed_t:
		return_t += (element,)

	return return_t

def sorted_key_list(d):
	"""Takes a dictionary as input, then puts the keys into a list of lists,
	then sorts the list by size of the sublists

	Keyword Arguments:
	d: The dictionary taken as input

	Return argument:
	l: the list of lists containing the keys
	"""

	l = []
	for element in d:
		l.append(d[element])
	l.sort(key=len, reverse = True)
	return l

def anagram_dictionary(wordlist):
	"""Takes a word list and returns a dictionary with each possible combination
	of letters from the words give as keys, and the words that can be made up with 
	those letters as values"""

	anagram_dictionary = dict()
	fin = open(wordlist)

	# Placeholder for the current word being checked to prevent redundancy 
	current_word = tuple()

	for line in fin:
		current_word = tuple_sort(tupled_string(line.strip()))

		if current_word not in anagram_dictionary:
			anagram_dictionary[current_word] = [line.strip()]
		else:
			anagram_dictionary[current_word].append(line.strip())

	return anagram_dictionary


def is_metathesis_pair(word_1, word_2):
	"""Takes two strings that are anagrams of each other as input and 
	returns true if two characters of the first can be switched to form the second"""

	# Since the two strings are anagrams, we know they are metathesis pairs if
	# and only if exactly 2 letters don't match
	non_match_count = 0

	for index in range(len(word_1)):
		if word_1[index] != word_2[index]:
			non_match_count += 1
	return non_match_count == 2

def print_metathesis_pairs(wordlist):
	"""Takes a string representing a wordlist file as input and prints
	all metathesis pairs as output

	Keyword Arguments:
	wordlist: file containing words that will be opened
	"""

	# Metathesis pairs are all anagrams, so this filters the possibilities
	ad = anagram_dictionary(wordlist)

	for key in ad:
		if len(ad[key]) > 1:
			for index in range(len(ad[key]) - 1):
				if is_metathesis_pair(ad[key][index], ad[key][index + 1]):
					print(ad[key][index], " ", ad[key][index + 1])

if __name__ == "__main__":
	print_metathesis_pairs("words.txt")