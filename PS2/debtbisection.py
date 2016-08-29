balance = input('Please enter a balance: ')
annualInterestRate = input('Please enter annual interest rate: ')

#this program will use bisection search to find lowest monthly payment

MONTHLYINTERESTRATE = annualInterestRate / 12.0 #constant
balanceCopy = balance

lower = balance / 12 #lower bound for bisection search
upper = (balance * ((1+MONTHLYINTERESTRATE)**12))/12.0 #upper bound

while True:
    monthlyPayment = (upper + lower) / 2
    for year in range(1,13): #does the calculations for 12 months (1 year)
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + (MONTHLYINTERESTRATE * monthlyUnpaidBalance)
    if balance > 0.01:
        lower = monthlyPayment
        balance = balanceCopy
    elif balance < -0.01:
        upper = monthlyPayment
        balance = balanceCopy
    else:
        break

print 'Lowest Payment:', str(round(monthlyPayment,2))
