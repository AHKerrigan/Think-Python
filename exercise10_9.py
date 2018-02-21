""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
s
Exercise 10-9:
Write a function that reads the file words.txt and builds a list with one element per
word. Write two versions of this function, one using the append method and the
other using the idiom t = t + [x]. Which one takes longer to run? Why? """

def file_list_append(file):
	"""Takes a file, then puts every line in the file into an element 
	of a list, then returns that list"""

	t = []

	fin = open(file)
	for line in fin:
		t.append(line)
	return t

def file_list_idiom(file):
	"""Takes a file as input, then uses operators to turn each line
	into an element of a list"""

	t = []

	fin = open(file)
	for line in fin:
		t = t + [line]
	return t

# print(len(file_list_append("words.txt")))
print(len(file_list_idiom("words.txt")))

# The idiom version is slower because the operator creates and entire new list