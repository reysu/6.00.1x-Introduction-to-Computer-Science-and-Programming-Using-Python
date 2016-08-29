def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    sumOfLists = 0                               #placeholder
    for num in range(len(listA)):                #loops through each index
        sumOfLists += (listA[num] * listB[num])  #adds the sum of two lists at one index to the variable
    return sumOfLists


dotProduct([-66, -51, -94, 73], [-92, 27, 65, -4])
