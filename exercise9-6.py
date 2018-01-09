e

def is_abecedarian(word):
	"""Receives a word as input and returns true if the letters in
	the word are in alphabetical order"""

	for i in range(len(word) - 1):
		if word[i] > word[i + 1]:
			return False
	return True

print(is_abecedarian('abcdef'))
print(is_abecedarian('abdxc'))

