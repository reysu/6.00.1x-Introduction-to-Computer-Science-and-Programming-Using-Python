def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    if exp == 0:
        return 1
    else:
       return base * recurPower(base, exp-1)


base = input("Please enter a base: ")
exp = input('Please enter a exponent: ')

print recurPower(base,exp)
