s1=int(input())
l1=[int(i) for i in input().split()]
c=0
for i in range(1,s1-1):
	if l1[i]<l1[i-1] and l1[i]<l1[i+1]:
		c+=1
	elif l1[i]>l1[i-1] and l1[i]>l1[i+1]:
		c+=1
print(c)
