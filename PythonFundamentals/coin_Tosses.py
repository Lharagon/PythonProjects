import math
import random

def coin_toss(attempts):
	heads = 0
	tails = 0

	for time in range(1, attempts + 1):
		ran_num = math.floor(random.random() * 2)
		if ran_num == 0:
			heads += 1
			print "Attempt #%s: Throwing a coin... It's a head! ... Got %s head(s) so far and %s tail(s) so far" % (time, heads, tails)
		elif ran_num == 1:
			tails += 1
			print "Attempt #%s: Throwing a coin... It's a tail! ... Got %s head(s) so far and %s tail(s) so far" % (time, heads, tails)

coin_toss(5000)