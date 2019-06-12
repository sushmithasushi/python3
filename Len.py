n1=int(input())
l1=list(map(int,input().split()))
m1=[]
a1=1
for i in range(n1-1):
    if l1[i]<l1[i+1]:
        a1+=1
    else:
        m1.append(a1)
        a1=1
m1.append(a1)
print(max(m1))
