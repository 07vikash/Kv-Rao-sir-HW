"""Q--> Write a python program which will decide whether the first character
        and last character of the given word is same or not?"""
x=input("Please type a word:")
if x[0]==x[-1]:
    print("Given word '{}' have same 1st and last character".format(x))
else:
    print("Given word '{}' haven't same !st and Last character".format(x))