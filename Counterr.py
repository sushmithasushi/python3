n1=int(input())
t1=3
s1=3
l1=[]
l1.append(3)
for i in range(1,n1+1):
    if t1==1:
        t1=2*s1
        s1=t1
        l1.append(t1)
    else:
        t1=t1-1
        l1.append(t1)
print(l1[n1-11])
