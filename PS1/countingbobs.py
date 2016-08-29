s = raw_input('Please enter a string: ')

bob_occurrences = 0

for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        bob_occurrences += 1
print 'Number of times bob occurs is:', bob_occurrences
