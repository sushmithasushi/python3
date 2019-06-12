p,q=map(int,input().split())
r=list(map(int,input().split()))
s=0
y=sorted(r)
x=(y[::-1])
for i in range(0,len(x)):
    a = q //(x[i])
    s = s + a
    q = q - (a *x[i])
print(u)
