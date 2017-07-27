name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(lst1, lst2):
	new_dict = {}

	for item in range(len(lst1)):
		new_dict[lst1[item]] = lst2[item]

	print new_dict

make_dict(favorite_animal, name)

# Hacker Challenge

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict2(lst1, lst2):
    keys = lst1
    values = lst2

    if len(lst1) < len(lst2):
        keys = lst2
        values = lst1

    pairs = zip(keys,values)
    new_dict = dict(pairs)

    print new_dict

make_dict2(favorite_animal, name)