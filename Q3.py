"""Q--> Write a Python program which will accept a word and decide
        whether it is palindrome or not?"""
x=input("Please Enter any word:")
if x[::1]==x[::-1]:
    print("Entered word '{}' is palindrome".format(x))
else:
    print("Entered word '{}' is not palindrome".format(x))