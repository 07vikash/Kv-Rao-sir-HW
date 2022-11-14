"""Q1--> Write a Python programm which accept the numerical value and finds the biggest
         amount of them by using ternary operator"""
x = int(input("Enter 1st Value:"))
y= int(input("Enter 2nd value:"))
z= int(input("Enter 3rd Value"))
if x>y and x>z:
    print("Biggest value is {} among your entered".format((x)))
elif y>z:
    print("Biggest value is {} among your entered".format((y)))
else:
    print("Biggest value is {} among your entered".format((z)))