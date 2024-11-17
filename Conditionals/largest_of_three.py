#Create a program to find the largest of three numbers.


number_1= int(input('Enter 1st number: '))
number_2= int(input('Enter 2nd number: '))
number_3= int(input('Enter 3rd number: '))

if (number_1>number_2):
    if (number_1>number_3):
        print(number_1)
    else:
        print(number_3)
elif (number_2>number_3):
    print(number_2)

else:
    print(number_3)
