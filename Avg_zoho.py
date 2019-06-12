p=int(input())
q=list(map(int,input().split()))
x1=y=u=k=0

for i in range(0,p-1):
    if i==0:
        x1=(x1+q[i])/(i+1)
    else:
        x1=0
        for t in range(0,i):
            x1=x1+q[t]
        x1 = (x1 + q[i]) // (i + 1)
    k=0
    for j in range(i+1,p):
        y=y+q[j]
        k=k+1
        if j==p-1:
            y=y//(k)
    if x1==y:
        u=1
        print("yes")
if u==0:
    print("no")
