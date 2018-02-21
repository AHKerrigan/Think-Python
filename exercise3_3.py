# Draw a 4x4 grid outlined on page 33
# We were only allowed to use functions here

def draw_grid():

	# functions for the + and - borders
	def top_border():
		print(('+----'*4)+'+')

	# The actual meat of the squares
	def inner_borders():
		print((('|    '*4)+'|'))
		print((('|    '*4)+'|'))
		print((('|    '*4)+'|'))
		print((('|    '*4)+'|'))

	# puts them together
	def full_row():
		top_border()
		inner_borders()
	full_row()
	full_row()
	full_row()
	full_row()
	top_border()
	

draw_grid()