def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    elif aStr[(len(aStr)/2)] == char: #checks if middle char is char
        return True

    else:
        if char > aStr[(len(aStr)/2)]:
            return isIn(char, aStr[len(aStr)/2:])
        else:
            return isIn(char, aStr[:len(aStr)/2])



print isIn('a', '')
print isIn('u', 'dls')
print isIn('z', 'bbkllmnrruuv')
print isIn('h', 'abddffghjjkqrrrtvvwz')
print isIn('i', 'efjv')
