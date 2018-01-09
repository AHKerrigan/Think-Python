""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-9:
“Recently I had a visit with my mom and we realized that the two digits that make up
my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered
how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six
times so far. I also figured out that if we’re lucky it would happen again in a few years,
and if we’re really lucky it would happen one more time after that. In other words, it
would have happened 8 times over all. So the question is, how old am I now?”
"""

def is_reversed(a, b):
	"""Takes two integers as inputs and determines if they are 
	reverses of each other"""

	# We convert the inputs to strings to make it easier to manipulate
	# For example 08 is 80 reversed but 08 is not an integer, 8 is
	astr = str(a)
	bstr = str(b)

	# We first use zfille to get the two strings to the same size
	if len(astr) > len(bstr):
		bstr = bstr.zfill(len(astr))
	if len(astr) < len(bstr):
		astr = astr.zfill(len(bstr))

	return astr == bstr[::-1]

def search_ages():
	"""Searches for solutions to the problem
	"""

	# Seems like a reasonable place to start
	child_start_age = 0
	mom_start_age = 16
	child_age = 0
	mom_age = 16
	true_age = 0

	reverse_count = 0

	# We iterate through mother starting ages
	while mom_start_age < 150:

		# For each starting age, we have to compare all possible ages (up until 150 is reasonable)
		for i in range(151 - mom_start_age):
			if(is_reversed(child_age, mom_age)):
				reverse_count = reverse_count + 1
				if reverse_count == 6:
					true_age = child_age
			child_age = child_age + 1
			mom_age = mom_age + 1

		if reverse_count == 8:
			print(true_age)
			break

		mom_start_age = mom_start_age + 1
		mom_age = mom_start_age
		child_age = 0







search_ages()