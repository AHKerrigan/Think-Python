""" This module contains code related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/



As an exercise, draw a stack diagram for print_n called with s = 'Hello' and n=2.
Then write a function called do_n that takes a function object and a number, n, as
arguments, and that calls the given function n times"""


""" Personal notes

When you actually pass a function, you do not include parameters, you are just passing
the function as a "thing". When you want to execute the function, you need to put the brackets
so that it actually runs as a function"""

def do_n(f, n):
	if n <= 0:
		return
	f()
	do_n(f, n - 1)

def say_Hello():
	print("Hello!")

do_n(say_Hello, 5)

