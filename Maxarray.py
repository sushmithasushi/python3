num,k1=map(int,input().split())
input()
a=list(map(int,input().split()))
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
	a.append(l[i])
	x=max(a)
	s.append(x)
print(*s)

