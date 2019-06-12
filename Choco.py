nu1=int(input())
k1=list(map(int,input().split()))
s1=[1]*nu1
for i in range(nu1):
    if i==0:
        if k1[i]>k1[i+1]:
            s1[i]=s1[i]+s1[i+1]
    elif i>0:
        if k1[i]>k1[i-1]:
            s1[i]=s1[i]+s1[i-1]
print(sum(s1))
