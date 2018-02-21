""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 11-3
Memoize the Ackermann function from Exercise 6-2 and see if memoization makes it
possible to evaluate the function with bigger arguments. Hint: no.
"""

known = {}
def ack(m, n):
	"""Takes a positive integer m and n and computes the ackermann function
	"""

	if (m, n) in known:
		return known[m, n]
	if m == 0:
		known[m, n] = n + 1
		return n + 1
	if m > 0 and n == 0:
		return ack(m - 1, 1)
	if m > 0 and n > 0:
		return ack(m - 1, ack(m, n-1))
 
print(ack(1, 1))
print(ack(3, 4))
print(ack(4, 5))