""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-2:
Write a function called cumsum that takes a list of numbers and returns the cumulative
sum; that is, a new list where the ith element is the sum of the first i+1 elements from
the original list.
"""

def cumsum(t):
	"""Takes in a list t as input and outputs a new list where each
	element is the cumulative sum of each ith element"""

	running_sum = 0
	for i in range(len(t)):
		t[i] = running_sum + t[i]
		running_sum = t[i]

	return t

t = [1, 2, 3, 4]
t = cumsum(t)
for x in t:
	print(x)