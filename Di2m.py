x11,y11=map(int,input().split())
if x11<=y11:
  d1=x11
else:
  d1=y11
z1=[]
for i in range(0,d1):
  z1.append(sorted(list(map(int,input().split()))))
c1=sorted(z1)
for i in range(0,len(c1[0])):
  for j1 in range(0,len(c1)-1):
    if c1[j1][i]>c1[j1+1][i]:
      c1[j1][i],c1[j1+1][i]=c1[j1+1][i],c1[j1][i]
for i in c1:
  print(*i)
