""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 6 Example 3:

As an exercise, write a function is_between(x, y, z) that returns True if x ≤ y ≤ z
or False otherwise.
"""

def is_between(x, y, z):
	return x <= y <= z

print(is_between(1,2,3))