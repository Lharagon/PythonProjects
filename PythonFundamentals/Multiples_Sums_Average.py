#Multiples Part I:

for num in range(1,1001):
	if num % 2 != 0:
		print num

#Multiples Part II:

for num in range(5,1000001):
	if num % 5 == 0:
		print num

#Sum List:

a = [1, 2, 5, 10, 255, 3]
sums = 0
for num in a:
	sums += num

print sums

#Average List:

a = [1, 2, 5, 10, 255, 3]

sums = 0
for num in a:
	sums += num

print sums/len(a)