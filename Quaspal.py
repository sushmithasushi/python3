numb=input()
n1=numb[::-1]
c1=0
if numb==n1:
	print("yes")
else:
	ss=numb[::-1]
	for i in range(len(ss)):
		if ss[i]=="0":
			s1=ss[i+1::]
			s2=s1[::-1]
			if s1==s2:
				c1=c1+1
			else:
				continue
		else:
			break
	if c1>0:
		print("yes")
	else:
		print("no")
