# Part I

def draw_stars(lst):

	for num in lst:
		print '*' * num

#Part II

def draw_stars2(lst):

	for num in lst:
		if type(num) == str:
			print num[0].lower() * len(num)
		else:
			print '*' * num


