#Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        


if __name__=="__main__":
    num=int(input("Enter an integer: "))

    if num < 0:
        print("Enter a positive integer.")
    else:
        print(f'Factorial of {num} = {factorial(num)}')
