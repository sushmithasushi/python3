import math
p=int(input())
q=math.log10(p)/math.log10(2)
if math.ceil(q)==math.floor(q):
	print(0)
else:
	r1=(p-1)//2
	u=r1*2
	print(p-u)
