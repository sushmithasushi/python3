r=int(input())
f=[int(i) for i in input().split()]
w=0
for i in range(r):
	for j in range(i):
		if f[j]<f[i]:
			w+=f[j]
print(w)
