""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 6-2:
Implement the Ackermann function and evaluate it for ack(3,4)"""

def ack(m, n):
	"""Takes a positive integer m and n and computes the ackermann function
	"""
	if m == 0:
		return n + 1
	if m > 0 and n == 0:
		return ack(m - 1, 1)
	if m > 0 and n > 0:
		return ack(m - 1, ack(m, n-1))


print(ack(3,4))