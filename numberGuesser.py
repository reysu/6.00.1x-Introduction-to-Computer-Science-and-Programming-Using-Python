#written by Eric Su
#Jun 25, 2016
#This program uses binary search to guess a number that you're thinking of
#that is between 0 and 100

print 'Please think of a number between 0 and 100!'
userHint = ''
low = 0
high = 100
while userHint != 'c':
    guess = (high+low)/2
    print 'Is your secret number', guess , '?'

    userHint = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.\
 Enter 'c' to indicate I guessed correctly.")

    if userHint == 'h':
        high = guess
    elif userHint == 'l':
        low = guess
    elif userHint != 'h' and userHint != 'l' and userHint != 'c':
        print 'Sorry, I did not understand your input'
print 'Game over. Your secret number was', guess
