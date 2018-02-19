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

import exercise10-1


##TODO: 
##Determine if we need reducible children
##Test the import
##Complete is_reducible
##Create fuction for finding largest word in a dictionary

def reducible_children(word, word_dict):
	"""Takes a string as input and returns a list of all words
	that can be created by removing one letter"

	Keyword Arguments:
	word: the string being reduced
	wordlist: the dictionary of words to check from

	Return Arguments:
	l: the list of reduced words"""

	current_word = ''

	return "Placeholder"

def is_reducible(word, word_dict):
	"""Takes a string and a dictionary as input and returns true 
	if one letter could be removed from that string to form
	a new word. Empty space is the base case

	Keyword Arguments:
	word: the word to be tested
	word_dict: a dictionary containing valid words"""


	if "a" not in string and "i" not in string:
		return False
	else:
		return True







if __name__ == "__main__":
	global reducible_words
	reducible_words = dict()
