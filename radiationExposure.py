def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def frange(start, end, step):
    tmp = start
    while(tmp < end):
        yield tmp
        tmp += step
def radiationExposure(start, stop, step):
    totalRadiation = 0

    for i in frange(start,stop,step): #width
    #    print 'rectangle width is', step
    #    print 'function value is ', f(i+step)
        radiation = step * f(i)
        totalRadiation += radiation
    #    print 'radiation is', radiation
        print 'Total radiation is', totalRadiation
    return totalRadiation

start = input('Start: ')
stop = input('Stop: ')
step = input('Step: ')

radiationExposure(start,stop,step)
