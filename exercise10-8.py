""" This is a solution to an exercise from

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/

Exercise 10-8:
Use random integers to estimate the probability that two people in the same room
will share a birthday given a room of 23 people """

import random

def has_duplicates(t):
	"""Takes a list as input and returns true if that list contains
	any duplicates"""

	# Each element will check each following elements for its duplicate
	# An element looking for duplicates before itself is redundant
	for i in range(len(t)):
		for n in t[i + 1:]:
			if t[i] == n:
				return True
	return False

def birthday_simulation():
	"""Generates a list of 23 birthdays and returns true if two people
	share a birthday"""

	birthdays = []

	for i in range(23):

		# Populates the list of birthdays with numbers between 1 and 365
		# We ignore leapyears
		birthdays.append(random.randint(1, 365))

	return has_duplicates(birthdays)

def birthday_interface():
	"""Prompts the user to enter the number of times they would like to run
	the birthday simulation, then outputs the number of times a duplicate
	was found"""

	
	while True:

		# The variable for the number of times the simulation finds a duplicate
		success = 0
		n = int(input("How many times would you like to run the birthday simulation (At least 10 reccomended)? Type 0 to end  \n"))
		if n == 0:
			break
		for i in range(n):
			if birthday_simulation():
				success += 1

		print("The chance that 2 people in a room of 23 share a birthday is about ", success / n * 100, "%\n")

birthday_interface()

