n1,a1,b1,c1=map(int,input().split())
li1=list(map(int,input.split()))
x=[]
for i in range(0,len(li)):
  for j in range(i,len(li)):
    for k in range(j,len(li)):
      x.append(a1*li[i]+b1*li[j]+c1*li[k])
print(max(x))
      
