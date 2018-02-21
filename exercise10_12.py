""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-12:
Two words “interlock” if taking alternating letters from each forms a new word. For
example, “shoe” and “cold” interlock to form “schooled”.

Write a program that finds all pairs of words that interlock. Hint: don’t enumerate
all pairs!
"""

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

def interlock(word1, word2):
	"""Takes two strings and interlocks the second to the first

	Keyword Arguments:
	word1: The string that will be the base
	word2: The string that will be interlocked to the first

	Return Arguments:
	result_word: The interlocked word"""

	word1_length = len(word1)
	word2_length = len(word2)
	result_word = ''

	# Because the strings may be different sizes, we want to be
	# able to continue to add the letters of the longer word one
	# once the first is exhausted

	if word2_length <= word1_length:
		for i in range(word2_length):
			result_word += (word1[i] + word2[i])

		# After the interlocking is done, we tack on any remaining letters
		# If they are the same, this simply adds nothing 
		result_word += word1[word2_length + 1: word1_length]
		return result_word
		
	# We do the same thing if word 2 is longer than word1
	else:
		for i in range(word1_length):
			result_word += (word1[i] + word2[i])

		result_word += word2[word1_length + 1: word2_length]
		return result_word





def is_interlocked_pair(word1, word2):
	"""Takes two strings as input and returns true if the words
	can be interlocked to form a new word"""


	# We use this file to check if interlocked they are a new word
	word_list = file_list_append('words.txt')

	# Checks to see if either combination creates a real word
	# in_bisect returns an integer if true, so we just check to see if its greater than -1
	if in_bisect(word_list, interlock(word1, word2)) > -1 or in_bisect(word_list, interlock(word2, word1)) > 1:
		return True
	else:
		return False		



def find_interlocked_pairs(file):
	"""Takes a file as input, then prints all pairs of interlocking
	words. Two words “interlock” if taking alternating letters from
	each forms a new word. For example, “shoe” and “cold” interlock 
	to form “schooled”.	

	Keyword Arguments:
	file: string that denotes a filname we read from"""

	# The list we will be looking in
	t = sorted(file_list_append(file))
	for i in range(len(t)):
		for x in range(i + 1, len(t)):
			print(i, x)
			if is_interlocked_pair(t[i], t[x]):
				print(t[i], t[x])

find_interlocked_pairs('words.txt')