""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-3:
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and
then print the number of words that don’t contain any of them. Can you find a combination
of five forbidden letters that excludes the smallest number of words?
"""

def avoids(word, forbidden):
	"""Takes a word and a string of forbiden chracters and returns true
	if the word contains none of the forbidden chararcters"""

	for letter in word:
		for forbidden_letter in forbidden:
			if letter == forbidden_letter:
				return False
	return True

def number_avoids(file, forbidden):
	"""Takes a filename as input and returns the numberof words that
	do not contain the forbidden characters"""

	fin = open(file)
	lines_avoided = 0 # The number of lines not containing the characters
	for line in fin:
		if avoids(line, forbidden):
			lines_avoided = lines_avoided + 1
	return lines_avoided

def number_of_lines(file):
	"""Takes a file and returns the number of lines that it has
	"""

	total = 0
	fin = open(file)
	for lines in file:
		total = total + 1
	return total

def excludes_least(file):
	"""Given a file, finds the 5 characters that exclude the least
	"""

	max_excluded = number_of_lines(file) # The max number of lines that can be excluded is the every line
	num1 = num2 = num3 = num4 = num5 = max_excluded # The variables that will represent each value 
	chr1 = chr2 = chr3 = chr4 = chr5 = '' # The letters themselves
	excluded = max_excluded # Used so we only have to calculate excluded once

	for c in 'abcdefghijklmnopqrstuvwxyz':
		excluded = max_excluded - number_avoids(file, c)
		if excluded < num1:
			num1 = excluded
			chr1 = c
		elif excluded < num2:
			num2 = excluded
			chr2 = c
		elif excluded < num3:
			num3 = excluded
			chr3 = c
		elif excluded < num4:
			num4 = excluded
			chr4 = c
		elif excluded < num5:
			num5 = excluded
			chr5 = c

	return chr1 + chr2 + chr3 + chr4 + chr5



forbidden = input("Enter the forbidden characters\n")
print("The number of words in the text file without those characters is", number_avoids("words.txt", forbidden))

# Note: For this solution, sorting algorithms had not been introduced yet so this is sort of brute forced

print("The characters that exclude the least number of lines are", excludes_least('words.txt'))