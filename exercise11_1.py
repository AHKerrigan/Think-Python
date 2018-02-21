""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 11-1
Write a function that reads the words in words.txt and stores them as keys in a dic‐
tionary. It doesn’t matter what the values are. Then you can use the in operator as a
fast way to check whether a string is in the dictionary.
"""


def to_dictionary(file):
	"""Takes a file as input and returns a dictionary containing
	each line as a key

	Keyword Arugments:
	file: the file we pull from

	Return aruguments:
	d: the dictionary we will return"""

	fin = open(file)
	d = dict()

	for line in fin:
		d[line.strip()] = ''
	return d


if __name__ == "__main__":

	d = to_dictionary('words.txt')
	print("hello")
	print('exercise' in d)
