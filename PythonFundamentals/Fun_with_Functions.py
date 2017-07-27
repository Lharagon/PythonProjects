# Odd/Even

def odd_even ():
    for num in range(1, 2000):
        if num % 2 == 0:
            print "Number is %s. This is an even number." % (num)
        else:
            print "Number is %s. This is an odd number." % (num)

# Multiply

def multiply(lst, mul):
	for num in range(len(lst)):
		lst[num] *= mul
	return lst

multiply([2,4,10,16], 5)

# Hacker Challenge

def layered_multiples(arr):
	new_array = []
	for num in range(len(arr)):
		new_array.append([1] * arr[num])
	print new_array

layered_multiples(multiply([2,4,10,16], 5))

