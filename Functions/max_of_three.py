#Create a function to find the maximum of three numbers.

def maxOfThree (number_1,number_2,number_3):
    if (number_1>number_2):
        if (number_1>number_3):
            return number_1
        else:
            return(number_3)
    elif (number_2>number_3):
        return number_2

    else:
        return(number_3)



if __name__=="__main__":
    
    number_1= int(input('Enter 1st number: '))
    number_2= int(input('Enter 2nd number: '))
    number_3= int(input('Enter 3rd number: '))

    print(f'Largest among {number_1},{number_2} and {number_3} is {maxOfThree(number_1,number_2,number_3)}')

    
    
    