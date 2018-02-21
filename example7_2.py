""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 7 Example 2:

Fix the "Make Way For Ducklings" example on page 87
"""

def abecedarian(prefixes, suffix):
	"""Takes a series of prefixes and attatches them to a suffix
	then prints them line by line"""
	for letter in prefixes:
		if letter == 'Q' or letter == 'O': # Fixes the problem in the original where words with Q or O are mispelled
			print(letter + 'u' + suffix)
		else:
			print(letter + suffix)

abecedarian('JKLMNOPQ', 'ack')