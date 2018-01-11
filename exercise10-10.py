""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-10:
Write a function called in_bisect that takes a sorted list and a target value and
returns the index of the value in the list if it’s there, or None if it’s not.
"""

def in_bisect(t, n):
	"""Takes in a list and sorts it, then returns the index of n
	if its contained in at list, returns None if it is not

	Keyword arguments:
	t: list to search through
	n: value to search for

	Return either an integer index or none
	"""

	# We sort the list so the algorithm works
	t = sorted(t)

	# These two variables will denote the lower and upper bound of our search
	search_space_upper = len(t) - 1
	search_space_lower = 0

	# If n is obviously outside the list we can just return None instantly
	if n < t[search_space_lower] or n > t[search_space_upper]:
		return None

	# The first bisect we perform is on the halfway mark
	bisect = int(search_space_upper / 2 )
	print(search_space_upper, search_space_lower)
	print(bisect)

	# If the bisect just happens to land on n, we now know where it is
	while not t[bisect] == n:
		
		if n < t[bisect]:

			# For both cases, if n is between the bisect and the next element
			# Then we know it cannot be in the list and we return None
			if t[bisect - 1] < n:
				return None
			search_space_upper = bisect

		if n > t[bisect]:
			if t[bisect + 1] > n:
				return None
			search_space_lower = bisect

		# We find the neww bisect by taking the average of the two
		bisect = int((search_space_upper + search_space_lower) / 2)

	return bisect

print(in_bisect([1, 2, 3, 4, 5, 7], 6))
print(in_bisect([1, 2, 3, 4, 5, 7], 5))