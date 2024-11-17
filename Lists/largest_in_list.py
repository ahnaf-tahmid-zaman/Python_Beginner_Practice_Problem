#Write a program to find the largest element in a list.

n=int(input("Enter the length of the list: "))

if n <=0:
    print("Please enter a positive integer...")
else:
    arr=[]
    
    for i in range(n):
        element=int(input(f'Enter the {i+1} element: '))
        arr.append(element)
    
    largestNum=arr[0]
        
    for i in arr:
        if i>=largestNum:
            largestNum=i
    
    print(f"The largest number in the list is: {largestNum}")


        