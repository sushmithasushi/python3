bs=int(input())
sb=[int(x) for x in input().split()]
r=[]
for i in range(0,len(sb)):
        y=sb[i:]
        z=max(y)
        if sb[i]==z:
                r.append(sb[i])
print(*r)
print(max(sb))
