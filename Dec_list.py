n1=int(input())
m1=list(map(int,input().split()))
d1=t=[]
for i in range(0,n1):
    d1=list(bin(m1[i]))
    d1=d1[2:]
    t.append(d1)
t=sorted(t)
t=t[::-1]
for i in range(0,n1):
    k1=1
    x=0
    for j in range(len(t[i])-1,-1,-1):
        x=x+(int(t[i][j])*k1)
        k1=k1*2
    print(x)
