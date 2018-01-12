""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-11:
Two words are a “reverse pair” if each is the reverse of the other. Write a program that
finds all the reverse pairs in the word list.
"""


"""My original solutions that employed a more brute force method"""

#def is_reverse_pair(word1, word2):
#	"""Takes in two strings and returns true is one is the reverse
#	of the other
#
#	Keyword arguments:
#	word1: first string
#	word2: second string
#
#	Returns a Boolean"""
#
#	return word1 == word2[::-1]
#
#def find_reverse_pairs(file):
#	"""Takes in a file as input and prints all reverse pairs
#
#	Keyword Arguments:
#	file: string containing the name of a filename
#	"""
#	# Creates the list of words
#	t = file_list_append(file)
#
#	# Sorts the words by string length
#	t.sort(key=len, reverse=False)
#
#	# Saves the list length for multiple use
#	n = len(t)
#
#	for i in range(n):
#		for x in range(i + 1, n):
#
#			# Two words of different length will not be the same, so this drastically cuts runtime
#			if len(t[i]) != len(t[x]):
#				break
#
#			if is_reverse_pair(t[i], t[x]):
#				print(t[i] + ' ' + t[x])
#
#find_reverse_pairs('words.txt')

def file_list_append(file):
	"""Takes a file, then puts every line in the file into an element 
	of a list, then returns that list

	Keyword Arguments:
	file: string that denotes a filename

	Return Arguments: 
	t: List containing all words from the file"""

	t = []

	fin = open(file)
	for line in fin:
		t.append(line.strip())
	return t



def in_bisect(t, n, needs_sorting = False):
	"""Takes in a list and sorts it if user requests, then returns the index of n
	if its contained in at list, returns None if it is not

	Keyword Arguments:
	t: list to search through
	n: value to search for
	needs_sorting: determines if the list needs to be sorted first

	Return either an integer index or none
	"""

	# We sort the list so the algorithm works
	if needs_sorting:
		t = sorted(t)

	# These two variables will denote the lower and upper bound of our search
	search_space_upper = len(t) - 1
	search_space_lower = 0

	# If n is obviously outside the list we can just return None instantly
	if n < t[search_space_lower] or n > t[search_space_upper]:
		return None

	# The first bisect we perform is on the halfway mark
	bisect = int(search_space_upper / 2 )

	# If the bisect just happens to land on n, we now know where it is
	while not t[bisect] == n:
		
		if n < t[bisect]:

			# For both cases, if n is between the bisect and the next element
			# Then we know it cannot be in the list and we return None
			if t[bisect - 1] < n:
				return None
			search_space_upper = bisect

		if n > t[bisect]:
			if t[bisect + 1] > n:
				return None
			search_space_lower = bisect

		# We find the neww bisect by taking the average of the two
		bisect = int((search_space_upper + search_space_lower) / 2)

	return bisect


def find_reverse_pairs(file):
	"""Takes in a file as input and prints all reverse pairs

	Keyword Arguments:
	file: string containing the name of a filename

	Return Arguments:
	None
	"""
	# Creates the list of words
	t = file_list_append(file)

	for line in t:
		if in_bisect(t, line[::-1]):
			print(line, line[::-1])

find_reverse_pairs('words.txt')


