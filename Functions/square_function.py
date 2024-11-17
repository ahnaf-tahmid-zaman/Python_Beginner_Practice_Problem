#Write a function that calculates the square of a number.


def square(n):
    return n*n

if __name__=="__main__":
    try:
        number=int(input("Enter a number: "))
        result=square(number)
        print(f'Square of {number} = {result}')
    except ValueError:
        print("Please enter a valid integer.")
    

