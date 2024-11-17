#Write a program that checks if a given number is positive, negative, or zero.


number = int(input("Enter a number: "))

if number == 0:
    print('Zero')
elif number < 0:
    print('Negative')
else:
    print('Positive')
