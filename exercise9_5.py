""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-5:
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many
words are there that use all the vowels aeiou? How about aeiouy?
"""

def uses_all(word, req_chr):
	"""Takes a word as input and returns true only if the word uses
	all of the characters from req_chr"""	


	flag = False
	# We loop through each required character and see if one of the characters is in the word
	for c in req_chr:
		for letters in word:
			if letters == c:
				flag = True

		# If we don't find the requisite character anywhere, we return false
		if flag == False:
			return False

		# We set it back to false so we can look for the next required character
		flag = False

	return True

print(uses_all("kerrigan", "eriz"))