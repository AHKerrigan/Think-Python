""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 13_1: 
Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
"""
import string

def file_to_list(filename):
	"""Takes a string representing a filename as input and outputs
	a list with each line as an element

	Keyword Arguments:
	filename: a string representing the name of a file

	Return Arguments:
	l: the list containing lines from the file"""

	fin = open(filename)
	l = []
	for line in fin:
		l.append(line.strip())
	return l

def file_to_words(filename):
	"""Takes a string representing a filename as input and ouputs
	a list with each seperate word as a element of a list

	Keyword Arguments:
	filename: a string representing the name of a file

	Return Arguments:
	l: the list containing words from the file"""
	
	line_list = file_to_list(filename)
	l = []

	# A string that holds all punctuation and whitespace characters
	# that we don't want
	strippables = string.whitespace + string.punctuation

	# Goes through each line, splits by whitespace, then removes
	# punctuation before putting the words into a list
	for line in line_list:
		line.replace("-", " ")
		for word in line.split():
			for symbol in strippables:
				word = word.strip(symbol)
			l.append(word.lower())
	return l

if __name__ == "__main__":

	print(file_to_words("sciencefiction.txt"))
	

