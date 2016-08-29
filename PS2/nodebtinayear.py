balance = input('Please enter a balance: ')
annualInterestRate = input('Please enter annual interest rate: ')


MONTHLYINTERESTRATE = annualInterestRate / 12.0 #constant

balanceCopy = balance #to save the original value
lowestPayment = 10 # the initial lowest payment, will increment by $10


while balance > 0: # loop only stops when it finds a lowest payment that allows balance to go below or equal to 0
    for year in range(1,13): #does the calculations for 12 months (1 year)
        monthlyUnpaidBalance = balance - lowestPayment
        balance = monthlyUnpaidBalance + (MONTHLYINTERESTRATE * monthlyUnpaidBalance)
        '''
        DEBUG:
        print 'Year:', str(year)
        print 'Monthly Unpaid:', str(monthlyUnpaidBalance)
        print 'balance:', str(balance)
        '''
    if balance > 0:
        balance = balanceCopy #resets the balance to original
        lowestPayment += 10 #increases lowest payment by 10

print 'Lowest payment:', lowestPayment
