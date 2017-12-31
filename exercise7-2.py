""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 7-2:
Write a function called eval_loop that iteratively prompts the user, takes the resulting
input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last
expression it evaluated.
"""

def eval_loop():
	"""Iteratively prompts the user to enter an input and evaluates it
	using python's "eval" function. Ends when the user inputs done.
	"""

	while True:
		user_input = input("Enter something to evaluate through the python interpreter. Enter done to quit")
		previous_input = None 
		
		# Because the language of the exercise seems to ask us to print the 
		# 'previous' input if the user enters done, we have to declare it as 
		# a seperate value then check to see if done is entered first, and 
		# only evaluate  it otherwise.
		if user_input == 'done':
			print(previous_input)
			break
		else:
			previous_input = user_input
			print(eval(user_input))

eval_loop()