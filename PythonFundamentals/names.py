
# Part I

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(lst):

	for student in range(len(lst)):
		print lst[student]['first_name'] + ' ' + lst[student]['last_name']


names(students)

# Part II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def user(dict):

    for users in dict:
        
        print users

        for person in range(len(dict[users])):
            first = dict[users][person]['first_name']
            last = dict[users][person]['last_name']
            length = len(first) + len(last)
            
            print "%s - %s %s - %s" % (person + 1,first,last,length)


user(users)
















