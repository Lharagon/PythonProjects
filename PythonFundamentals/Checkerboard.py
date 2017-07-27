size = 8

for row in range(1,size + 1):
    if row % 2 != 0:
        pattern = ''
        for column in range(1,size + 1):
            if column % 2 == 0:
                pattern += "*"
            else:
                pattern += " "
    else:
        pattern = ''
        for column in range(1,size + 1):
            if column % 2 == 0:
                pattern += " "
            else:
                pattern += "*"
    print pattern
    
