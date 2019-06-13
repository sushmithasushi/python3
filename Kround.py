bb=input().split()
k1=int(bb[1])
n1=int(bb[0])
bb=[int(d) for d in bb[0]]
f=0
p=1;
while(f==0):
	prod=p*n1
	l=[ int(d) for d in str(prod)]
	c=0
	j=len(l)-1
	while(l[j]==0):
		c+=1
		j-=1
	if(c>=k1):
		print(prod)
		f=1
	p+=1
