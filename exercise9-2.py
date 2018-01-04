""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 8-5:
Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it.
Modify your program from the previous section to print only the words that have no
“e” and compute the percentage of the words in the list that have no “e”.
"""

def has_no_e(phrase):
	"""Takes a string as input and returns true if and 
	only if it does not contain the letter 'e'"""

	for c in phrase:
		if c == 'e':
			return False
	return True

def percent_no_e(file):
	"""Takes a filename as input and returns the percentage of words
	that do not contain the letter 'e'"""

	fin = open(file)
	total_lines = 0.0
	total_no_e = 0.0

	# Checks each line for words that have no e while also counting the lines
	for line in fin:
		if has_no_e(line.strip()):
			total_no_e = total_no_e + 1
		total_lines = total_lines + 1

	return (total_no_e/ total_lines) * 100.0

print(percent_no_e("words.txt"))

