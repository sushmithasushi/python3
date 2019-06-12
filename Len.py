inp=int(input())
li=list(map(int,input().split()))
m=[]
c=1
for i in range(n-1):
	if li[i]<li[i+1]:
		c+=1
	else:
		m.append(c)
		c=1
m.append(c)
print(max(m))
