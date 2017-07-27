# Find and Replace

str = "It's thanksgiving day. It's my birthday, too!"
str.find("day") ##### 18
new_string = str.replace("day", "month", 1)
print new_string ##### "It's thanksgiving month. It's my birday, too!"

# Min and Max

x = ["hello", 2, 54, -2, 7, 12, 98]

min(x)
	#>>>>>>>> -2
max(x)
	#>>>>>>>> 98

# First and Last

z = ["hello", 2,54,-2,7,12,98,"world"]

new_z = []
new_z.append(z[0])
new_z.append(z[len(z) - 1])
print new_z

#New List

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x = sorted(x)
f_half = x[:len(x)/2]
s_half = x[len(x)/2:]

s_half.insert(0, f_half)

print s_half #>>>>>> [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

