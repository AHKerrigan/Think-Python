""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-6:
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are
anagrams."""

import time

def is_anagram(word1, word2):
	"""Takes two strings as input and returns true if they
	are anagrams of each other, false otherwise"""

	word2_list = list(word2)


	# The strategy is whittle down a list version of the second word
	# by matching them to a letter from word one
	for c1 in word1:
		for i in range((len(word2_list) )):
			if word2_list[i] == c1:
				del word2_list[i]
				break

	# The words are anagrams if the list we created finds a partner for each element
	# and therefore is completely stripped
	return word2_list == []

def is_anagram_book(word1, word2):
	"""The solution from the book, for reference"""
	return sorted(word1) == sorted(word2)


print(is_anagram("stuff", "ftufs")
