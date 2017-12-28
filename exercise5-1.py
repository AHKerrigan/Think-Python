""" This module contains code related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 5-1: Write a script that reads the current time and converts it to a time of day in hours,
minutes, and seconds, plus the number of days since the epoch.
"""
import time

# This could be done more efficiently using a recursive function, but that would require an array 
# which has not been introduced yet in the book so I just used this method. 

def find_unit(t, n):
	"""calculates the number of time units, given the number of seconds and the time per unit
	"""
	return t // n

def reduce_time(t, n):
	"""Factors out the remaining seconds given the seconds in some time unit
	""" 
	return t % n

t = time.time()
days = find_unit(t, 60*60*24)
t = reduce_time(t, 60*60*24)
hours = find_unit(t, 60*60)
t = reduce_time(t, 60*60)
minutes = find_unit(t, 60)
t = reduce_time(t, 60)

print("It has been ", days, "days, ", hours, "hours, ", minutes, "minutes, and ", int(t), "seconds since the UNIX epoch")