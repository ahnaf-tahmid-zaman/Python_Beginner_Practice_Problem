#Check if a string contains only vowels.


string = input('Enter a string: ').lower()

only_vowels = True
for char in string:
    if char not in 'aeiou':
        only_vowels = False
        break

if only_vowels:
    print(f'{string}: only contains vowels.')
else:
    print(f'{string}: does not only contain vowels.')
