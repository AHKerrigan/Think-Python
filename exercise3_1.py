# Function that takes a string a displays it so that the last letter appears in collumn 70
def right_justify(string):
	
	
	chars = len(string) # Number of characters in the string
	return (' '*(70-chars)) + string #returns string with appropriate number of spaces

print(right_justify('monty'))