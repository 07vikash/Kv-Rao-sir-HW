t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    l1=[a,b,c]
    cn=0
    for i in l1:
        if i>=(sum(l1)/3):
            cn=cn+1
    if cn>=2:
        print("pass")
    else:
        print("no")