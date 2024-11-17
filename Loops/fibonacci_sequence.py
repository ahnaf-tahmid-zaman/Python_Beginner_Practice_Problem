#Generate the Fibonacci sequence up to n terms.

term=int(input("Enter the sequence: "))

a,b=0,1

if term <= 0:
    print("Plesae enter a positive integer number...")
elif term == 1:
    print(a)
else:
    for _ in range(term):
        print(a,end=" ")
        a,b=b,a+b

print("\n")

