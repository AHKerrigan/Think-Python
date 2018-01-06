""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-7:
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-pp-
i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?
"""

def triplet_skip(word, i):
	"""Takes a string and an i as input and returns a string made up
	of a triplet of every other character starting at i"""

	return word[i] + word[i + 2] + word[i + 4]

def triple_consecutive_letters(word):
	"""Takes a word as input and outputs true is that word contains three
	consecutive double letters"""

	# If a word has three consecutive double letters, then a series of three letters
	# skipping every letter would be the same starting at i and i+1
	for i in range(len(word) - 5):
		 if triplet_skip(word, i) == triplet_skip(word, i + 1):
		 	return True

	return False

fin = open("words.txt")
for line in fin:
	if triple_consecutive_letters(line.strip()):
		print(line.strip())