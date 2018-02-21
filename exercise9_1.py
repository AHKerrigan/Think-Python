""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 8-5:
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
"""


def short_words(filename, n):
	"""Takes in a filename and prints only the words with no more than
	n words"""

	fin = open(filename)
	for line in fin:
		word = line.strip()
		if len(word) <= n:
			print(word)

short_words("words.txt", 20)

