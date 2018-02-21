""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 6-5:
Write a function called gcd that takes parameters a and b and returns their greatest common divisor"""

def gcd(a,b):
	"""Takes two values a and b and returns their greatest common divisor
	"""
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

print(gcd(105, 25))