""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-4:
Write a function called chop that takes a list, modifies it by removing the first and last
elements, and returns None."""

def chop(t):
	"""Takes in a list and deleted the first and last elements, 
	then returns None"""

	del t[0]
	del t[-1]

t = [1, 2, 3, 4]
chop(t)
print(t)