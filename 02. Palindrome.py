x = input("Enter string: ")
rev = x[::-1]
if x == rev:
    print(x, "is a palindrome.")
else:
    print(x, "is not a palindrome.")
