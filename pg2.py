word = input("Enter string: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")