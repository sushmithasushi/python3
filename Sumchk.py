n1,k1=map(int,input().split())
a1=list(map(int,input().split()))
b1=a1[:]
c=0
s=0
for i in a1:
    b1.remove(i)
    for j in b1:
        if(s==0):
            if(i+j==k1):
                print("yes")
                c=c+1
                s=s+1
    b1=a1[:]
if(c==0):
    print("no")
