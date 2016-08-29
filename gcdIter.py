def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testVal = min(a,b)
    while (a % testVal != 0) or (b % testVal !=0):
        testVal -= 1
    return testVal

a = input('a: ')
b = input('b: ')

print gcdIter(a,b)
