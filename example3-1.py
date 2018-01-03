# If you have repeat lyrics first, you don't get an error, but you also don't get an output


def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and I work all day.")

# The location of these definitions are irrelevent, because they are called after they are both defined

repeat_lyrics()