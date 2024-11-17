#Count the number of vowels and consonants in a string.

inputString=str(input("Enter a string: "))

countVowel=0
countConsonants=0
vowels='aeiouAEIOU'

for char in inputString:
    if char.isalpha():
        if char in vowels:
            countVowel+=1
        else:
            countConsonants+=1

print(f'Number of vowels in {inputString} = {countVowel}\nNumber of consonents in {inputString} = {countConsonants}')

