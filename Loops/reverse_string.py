#Write a program that reverses a string.


string=input("Enter a string: ")

reversed_string=""

for char in string:
    reversed_string=char+reversed_string

print(reversed_string)
