balance = input('Please enter a balance: ')
annualInterestRate = input('Please enter annual interest rate: ')
monthlyPaymentRate = input('Please enter a monthly payment rate: ')


MONTHLYINTERESTRATE = annualInterestRate/12.0 #constant
totalPaid = 0 #counter to track how much you paid

for year in range(1,13): #does this for every month of the year
    print 'Month:', str(year)
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid += minimumMonthlyPayment #adds the monthly payment to the total
    print 'Minimum monthly payment:', str(round(minimumMonthlyPayment,2))
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (MONTHLYINTERESTRATE * monthlyUnpaidBalance) #this becomes remaining balance
    print 'Remaining balance:', str(round(balance,2))

print 'Total paid:', str(round(totalPaid,2))
print 'Remaining balance:', str(round(balance,2))
