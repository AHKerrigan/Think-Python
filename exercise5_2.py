""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 5-2: 
1: Write a function that takes a, b, c, and n and checks if 
Fermat's Last Theorem holds
2: Write a function that prompts the user to enter their own input values.
"""

def check_fermat(a,b,c,n):
	"""Takes a, b, c, and n and checks to see if fermat's last theorem
	holds, oututting a text result"""
	if n <= 2:
		print("Please enter an n greater than or equal to 2")

	elif a**n + b**n == c**n:
		print("Holy smokes, Fermat was wrong!")

	else:
		print("No, that doesn't work")

def input_fermat():
	"""Prompts the user to enter an a, b, c, and n, then checks to see if
	they satisfy the equation a^n + b^n = c^n"""
	a = int(input('Enter a value for a\n'))
	b = int(input('Enter a value for b\n'))
	c = int(input('Enter a value for c\n'))
	n = int(input('Enter a value for n\n'))

	check_fermat(a, b, c, n)

input_fermat()

