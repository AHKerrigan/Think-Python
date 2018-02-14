""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 12-2: 
1. Write a program that reads a word list from a file (see “Reading Word Lists” on
page 99) and prints all the sets of words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters
to a list of words that can be spelled with those letters. The question is, how can
you represent the collection of letters in a way that can be used as a key?
2. Modify the previous program so that it prints the longest list of anagrams first,
followed by the second longest, and so on.
3. In Scrabble, a “bingo” is when you play all seven tiles in your rack, along with a
letter on the board, to form an eight-letter word. What collection of eight letters
forms the most possible bingos? Hint: there are seven.
Solution: http://thinkpython2.com/code/anagram_sets.py.
"""

# TODO: Sorting a tuple turns it into a list, and therefore current_word
# cannot be hashed, figure out solution
def tupled_string(phrase):
	"""Takes a string as input and returns a tuple with each
	letter as an element"""

	# The tuple to be returned
	ts = tuple()

	for element in phrase:
		ts = ts + (element,)

	return ts

def print_anagram_sets(wordlist):
	"""Takes a word list in the form of a string and prints out all
	the sets of words that are anagrams."""

	anagram_dictionary = dict()
	fin = open(wordlist)

	# Placeholder for the current word being checked to prevent redundancy 
	current_word = tuple()

	for line in fin:
		current_word = sorted(tupled_string(line.strip()))
		print(type(current_word))

		if current_word not in anagram_dictionary:
			anagram_dictionary[current_word] = [line.stip()]
		else:
			anagram_dictionary[current_word].append(line)

	for element in anagram_dictionary:
		if len(anagram_dictionary[element]) > 1:
			print(anagram_dictionary[element])

print(type(sorted(tupled_string("Hi"))))