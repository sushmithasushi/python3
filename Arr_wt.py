n1,w1=map(int,input().split())
p1=list(map(int,input().split()))
v1=list(map(int,input().split()))
r1=[]
c1=0
for i in range(n1):
    x1=v1[i]/p1[i]
    r1.append(x1)
while w1>=0 and len(r1)>0:
    mindex=r1.index(max(r1))
    if w1>=p1[mindex]:
        c1=c1+v1[mindex]
        w1=w1-p1[mindex]
    p1.pop(mindex)
    v1.pop(mindex)
    r1.pop(mindex)
print(c1)
