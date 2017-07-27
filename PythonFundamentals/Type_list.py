

#Type list assignment

inputs = ['magical unicorns',19,'hello',98.98,'world']




the_string = ''
the_number = 0

for thing in inputs:
    if isinstance(thing, int) == True or isinstance(thing, float) == True:
        the_number += thing
    elif isinstance(thing, str) == True:
        the_string += thing
    else:
        print "Cant really do much with ", thing
print "The string: ",the_string
print the_number
    