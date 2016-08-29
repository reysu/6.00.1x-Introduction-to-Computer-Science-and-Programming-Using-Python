def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    newList = []                                #to store the flattened List
    for x in aList:                             #loop through each item
        if type(x) != list:                     #if it isn't a list, add it to the newList
            newList.append(x)
        else:                                   #if it is a list, recursively go in and add it to the newList
            newList.extend(flatten(x))
    return newList

flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])  #[1,'a','cat',2,3,'dog',4,5]





'''

def flatten(x):
    try:
        it = iter(x)
    except TypeError:
        yield x
    else:
        for i in it:
            for j in flatten(i):
                yield j
'''
