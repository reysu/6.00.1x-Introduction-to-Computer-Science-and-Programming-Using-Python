#oops I did this wrong and made it more complicated than it needs to be
#i thought I still had to use successive addition but I could use successive multiplication
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 0
    exps = 0
    if exp == 2 or exp == 3:
        exps = 1
    if exp == 0:
        print 1
    elif exp == 1:
        print base
    else:
        while exp > exps:
            for num in range(base):       #(base + base) base times
                result += base
            exp -= 1
        #    print 'result is',result
        #    print 'exp is', exp
        print result

base = input('Please enter a base: ')
exp = input('Please enter a exp ')
iterPower(base,exp)
