list_one = [1,2,3,6,2,5]
list_two = [1,2,3,6,2,5]


def same_check(l1, l2):
    if len(l1) == len(l2):
        counter = 0
        for item in l1:
            if item == l2[counter]:
                counter += 1
            else:
                print "The lists are not the same"
                break
        else:
            print "The lists are the same"
    else:
        print "Not the same"
           
        
same_check(list_one, list_two)