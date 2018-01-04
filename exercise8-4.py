""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 8-4:
The following functions are all intended to check whether a string contains any lowercase
letters, but at least some of them are wrong. For each function, describe what the
function actually does (assuming that the parameter is a string).
"""

def any_lowercase1(s): 
	"""Takes a string as input and returns true if the first letter 
	is lowercase, returns false otherwise"""
	for c in s:
		if c.islower():
			return True
		else:
			return False

def any_lowercase2(s):
	"""Always returns true because 'c' is lowercase
	"""
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'

def any_lowercase3(s):
	"""Takes a letter as input and returns whether the last
	letter is true or now"""
	for c in s:
		flag = c.islower()
	return flag

def any_lowercase4(s):
	"""Takes a string as input and returns true if it contains
	any lowercase characters"""
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

def any_lowercase5(s):
	"""Takes a string as input and returns true only if the
	string contains no uppercase characters"""
	for c in s:
		if not c.islower():
			return False
	return True

print(any_lowercase4('KERRIGAN'))