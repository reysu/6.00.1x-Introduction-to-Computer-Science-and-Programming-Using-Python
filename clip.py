def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    print min(max(x,lo),hi)
    #print max(min(lo,hi),x)
clip(5,6,7) # return 6

clip(7,8,3) # return 3

clip(7,2,3) # return 2

clip(-4.41, -5.35, 6.95)
