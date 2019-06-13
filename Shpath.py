t,u=map(int,input().split())
x=[]
for i in range(u):
   x.append(list(map(int,input().split())))
cost=10000000
f=0
for i in range(u):
  if x[i][0]==1:
    s=x[i][1]
    c=x[i][2]
    for j in range(i+1,u):
      if x[j][0]==s:
        s=x[j][1]
        c+=x[j][2]
    if c<cost and s==t:
      cost=c
      f+=1
if f==0:
  print(-1)
else:
  print(cost)
