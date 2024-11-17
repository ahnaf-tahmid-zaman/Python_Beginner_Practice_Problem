#Write a function to check if a string is a palindrome.

def checkPalindrome(string):
    string=string.replace(" ","").lower()
    reversedString=string[::-1]

    return string==reversedString

if __name__=="__main__":
    string=input("Enter a string: ")
    isPalindrome=checkPalindrome(string)

    if isPalindrome:
        print("Palindeome")
    else:
        print("Not palindrome")



