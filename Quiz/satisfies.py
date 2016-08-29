def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    newList = []                    #this will contain all the True elements
    for i in range(len(L)):
        if f(L[i]):                 #so go through each item, if it is true
            newList.append(L[i])    #add it to the new list
    L[:] = newList                  #convert L to the new LIst
    return len(L)                   #return the length of it
run_satisfiesF(L, satisfiesF)
