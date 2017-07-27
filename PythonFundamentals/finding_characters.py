l = ['hello','world','my','name','is','Anna', 'you', 'are', 'not','the','father']
char = 'o'
new_list = []

for index in l:
    for letter in index:
        if letter == char:
            new_list.append(index)

print new_list