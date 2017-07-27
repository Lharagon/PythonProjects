for num in range(100,100000):
    output = 'Foo', 'prime', num
    for number in range(2, num/2):
        if num % number == 0:
            output = 'FooBar'

    for number in range(1, 500):
        if number * number == num:
            output = 'Bar', 'square', num
    print output
