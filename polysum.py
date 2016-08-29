import math
def polysum(n,s):
    '''
    function takes two numbers
    will sum the area and square of the perimeter of the regular polygon
    function will return sum, rounded to 4 decimal places
    '''

    area = (0.25*n*math.pow(s,2))/(math.tan(math.pi/n)) #given function to find area
    square_of_perimeter = math.pow((n * s),2) #the square of the perimeter
    return round(area + square_of_perimeter,4) #the sum of area and square of perimeter to four decimal points
