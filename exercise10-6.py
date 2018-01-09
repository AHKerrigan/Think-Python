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

def is_anagram(word1, word2):
	"""Takes two strings as input and returns true if they
	are anagrams of each other, false otherwise"""

	word2_list = list(word2)

	for c1 in word1:
		for i in range((len(word2_list) )):
			print(i)

is_anagram("stuff", "things")
