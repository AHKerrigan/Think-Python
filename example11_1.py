""" This is a solution to an example from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Chapter 11 Example 1:

Write histograms more concisly 
"""

def historgram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

print(historgram('brontosaurus'))