""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 9-8:
“I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I’d see 3-0-0-0-0-0. “Now, what I saw that day was very interesting. 
I noticed that the last 4 digits were palindromic; that is, they read the same forward as 
backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?”
"""

def is_palindrome_num(number):
	"""Takes an integer as input and returns true if it is a palindrome
	"""
	return (str(number)) == (str(number))[::-1]

def is_palindrome(string):
	"""Takes a string as input and returns true if it is a palindrome
	"""
	return string == string[::-1]

def partial_palindrome(string, start, end):
	"""Takes a string as well as a start and end point and returns true
	if that section of the string is a palindome"""
	return is_palindrome(string[start:end])

def test_cases():
	"""Runs through 6 digit numbers and tests if they can follow the rule
	given in the problem statement"""
	
	for i in range(100000,999999):
		if (partial_palindrome(str(i), 2, 6) and 
			partial_palindrome(str(i + 1), 1, 6) and
			partial_palindrome(str(i + 2), 1, 5) and
			partial_palindrome(str(i + 3), 0, 6)):

			print(i)


test_cases()