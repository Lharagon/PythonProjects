import random
import math

def score_grade():
	for time in range(10):
		ran_num = math.floor((random.random() * (100 - 60)) + 60)

		if ran_num >= 90:
			print "Score: %s; Your grade is A" % (ran_num)
		elif ran_num >= 80:
			print "Score: %s; Your grade is B" % (ran_num)
		elif ran_num >= 70:
			print "Score: %s; Your grade is C" % (ran_num)
		elif ran_num >= 60:
			print "Score: %s; Your grade is D" % (ran_num)

score_grade()