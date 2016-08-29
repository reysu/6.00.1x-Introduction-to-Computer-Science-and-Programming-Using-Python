def f(a,b):
    return a + b
def dict_interdiff(d1,d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}                   #dictionary datatype
    difference = {}                  #dictionary datatype
    d1_backup = d1.copy()
    d2_backup = d2.copy()
    for x in d1:
        for y in d2:
            if x == y:
                intersect[x] = f(d1[x],d2[y])

    for a in d1:                 #loop over key and value
        for c in d2:
            if a == c:
                del d1_backup[a]
                del d2_backup[c]
    difference = dict(d1_backup.items() + d2_backup.items())

    int_diff_tuple = (intersect, difference)  #tuple of two dictionaries
    return int_diff_tuple

dict_interdiff({1:30, 2:20, 3:30, 5:80},{1:40, 2:50, 3:60, 4:70, 6:90})
