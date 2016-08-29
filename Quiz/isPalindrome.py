def isPalindrome(aString):
    '''
    aString: a string
    returns a boolean
    '''
    new = '' #placeholder
    if len(aString) <= 1:
        print 'True'
        return True
    elif aString[0] == aString[-1]: #if first and last letter are the same
            new = aString[1:-1]       #new string is just the middle
            return isPalindrome(new)
    else:
        print 'False'
        return False

isPalindrome('')           #True
isPalindrome('OVIXih')     #False
isPalindrome('YQEQY')      #True
isPalindrome('slLKjwnNu')  #False
isPalindrome('fdf')        #True
isPalindrome('N')          #True
isPalindrome('hlWjvvjWlh') #True
isPalindrome('TmGyCqnXO')  #False
isPalindrome('lgiigl')     #True
isPalindrome('GXOvLgg')    #False





'''
isPalindrome('dammitimmad')        #True
isPalindrome('abuttuba')           #True
isPalindrome('acaramanamaraca')    #True
isPalindrome('anutforajaroftuna')  #True
isPalindrome('applesandoranges')  #false
isPalindrome('himynameisericsu')  #false
isPalindrome('asantbatnasa')      #false
'''
