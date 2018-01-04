""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-4:
Write a function named uses_only that takes a word and a string of letters, and that
returns True if the word contains only letters in the list.

Can you make a sentence using only the letters acefhlo?”
"""

def uses_only(word, req_chr):
	"""Takes a word and returns true only if it uses only
	the letters in req_chr"""

	for letters in word:
		flag = False

		# Goes through each letter in word and looks for it to be at least one of the characters in req_chr
		# Will return false otherwise
		for c in req_chr:
			if c == letters:
				flag = True
		if not flag:
			return False

	return True

print(uses_only('kerrigan', 'keigan'))
fin = open("words.txt")
for line in fin:
	if uses_only(line.strip(), 'acefhlo'):
		print(line.strip())