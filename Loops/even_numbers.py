#Print all even numbers between 1 and 100.


for i in range(1,101):
    if (i%2==0):
        print(i, end=', ' if i<100 else '\n')

    
#alternative

print(', '.join(str(i) for i in range(2,101,2)))
