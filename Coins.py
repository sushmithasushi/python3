p,q=map(int,input().split())
r=list(map(int,input().split()))
s=0
y=sorted(t)
x=(y[::-1])
for i in range(0,len(x)):
    z = q //(x[i])
    s = s + z
    q = q - (z *x[i])
print(u)
