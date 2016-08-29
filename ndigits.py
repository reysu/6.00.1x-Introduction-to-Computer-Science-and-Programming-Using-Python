def ndigits(x):
    if abs(x)/10 == 0:
        return 1
    else:
         return 1 + ndigits(abs(x) / 10)
   
