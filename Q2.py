""" Q--> Write a python program which will accept 3 numerical value and
         find biggest and smallest and check equality? """
l1=[]

for i in range(1,4):
    val=int(input("Please enter {} value:".format(i)))
    l1.append(val)
l2=l1.copy()
print("You Entered These Value: {}".format(l2))
s=l1.sort()
if l1[0]!=l1[1]!=l1[2]:
    print("Biggest value is {}".format(l1[-1]))
    print("Smallest value is {}".format(l1[0]))
elif l2[0]==l2[1] and l2[0]!=l2[2]:
    print("1st Value {} and 2nd value {} is equal".format(l2[0],l2[1]))
    print("Biggest value is {}".format(l1[-1]))
    print("Smallest value is {}".format(l1[0]))
elif l2[1]==l2[2] and l2[0]!=l2[1]:
    print("2nd Value {} and 3rd value {} is equal".format(l2[1], l2[2]))
    print("Biggest value is {}".format(l1[-1]))
    print("Smallest value is {}".format(l1[0]))
elif l2[0]==l2[2] and l2[2]!=l2[1]:
    print("1st Value {} and 3rd value {} is equal".format(l2[0], l2[2]))
    print("Biggest value is {}".format(l1[-1]))
    print("Smallest value is {}".format(l1[0]))
else:
    print("All are equal ")