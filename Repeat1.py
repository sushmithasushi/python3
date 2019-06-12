nu=int(input())
a=[]
k1=bin(2**nu-1)[2::]
l1=len(k1)
for i in range(0,2**nu):
	s1=bin(i1)[2::]
	if len(s1)<l1:
		a1.append([s1.count("1"),(l1-len(s1))*"0"+s1])
	else:
		a1.append([s1.count("1"),s1])
a.sort()
for i in range(0,len(a)):
	print(a1[i1][1])
