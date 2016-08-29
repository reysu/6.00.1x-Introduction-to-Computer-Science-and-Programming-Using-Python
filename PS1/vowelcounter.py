s = raw_input('Please enter a string: ')
vowel_occurrences = 0

for vowel in 'aeiouAEIOU':
    for letter in s:
        if vowel == letter:
            vowel_occurrences += 1

print 'Number of vowels:', vowel_occurrences
