a=int(input())
s=list(map(int,input().split()))
y=sorted(s)[::-1]
z=""
if(s==[0]*a):
    print("0")
else:
    for j in y:
        z=z+str(j)
    print(int(z))
