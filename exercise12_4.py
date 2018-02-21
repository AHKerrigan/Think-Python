""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 12-4: 
What is the longest English word, that remains a valid English word, as you remove its
letters one at a time?

Now, letters can be removed from either end, or the middle, but you can’t rearrange
any of the letters. Every time you drop a letter, you wind up with another English
word. If you do that, you’re eventually going to wind up with one letter and that too is
going to be an English word—one that’s found in the dictionary. I want to know what’s
the longest word and how many letters does it have?

I’m going to give you a little modest example: Sprite. Ok? You start off with sprite, you
take a letter off, one from the interior of the word, take the r away, and we’re left with
the word spite, then we take the e off the end, we’re left with spit, we take the s off,
we’re left with pit, it, and I.
"""

from exercise11_1 import to_dictionary


##TODO: 
##Create fuction for finding largest word in a dictionary


def is_reducible(word, word_dict):
	"""Takes a string and a dictionary as input and returns true 
	if one letter could be removed from that string to form
	a new word. Empty space is the base case

	Keyword Arguments:
	word: the word to be tested
	word_dict: a dictionary containing valid words"""


	# The base cases, as well as checking the memo

	if "a" not in word and "i" not in word:
		return False
	if word in reducible_words:
		return True
	if word == 'a' or word == 'i':
		return True

	# The function is recursive, looking for one reduction, then
	# checking until the base case or a memoized word is found
	word_length = len(word)
	for i in range(word_length):
		current_reduction = word[0:i] + word[i + 1:word_length]
		if current_reduction in word_dict and is_reducible(current_reduction, word_dict):
			reducible_words[word] = word_length
			return True

def most_reducible(wordlist):
	"""Takes in a wordlist file as input and prints the longest 
	word that can be reduced into other words one letter at a time

	Keyword Arguments:
	wordlist: a string that represents the list of words we will
	look from
	"""

	# We create a memo for reducible words since is_reducible is 
	# recursive. The keys are the words and the values are the 
	# number of characters
	global reducible_words
	reducible_words = dict()
	reducible_words['a'], reducible_words['i'] = 1, 1
	
	word_dict = to_dictionary(wordlist)
	for line in word_dict:
		is_reducible(line, word_dict)

	# Varible that will search the memo for the longest word
	current_greatest = ''
	for word in reducible_words:
		if reducible_words[word] > len(current_greatest):
			current_greatest = word
	print(current_greatest)

if __name__ == "__main__":
	most_reducible("words.txt")

	