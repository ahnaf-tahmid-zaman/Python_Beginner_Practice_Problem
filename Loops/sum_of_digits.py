#Find the sum of digits of a given number.


number=int(input("Enter a number: "))
totalSum=0
while (number!=0):
    totalSum+=number%10
    number//=10

print(totalSum)
