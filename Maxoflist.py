n1,a1,b1,c1=map(int,input().split())
li1=list(map(int,input.split()))
f=[]
for i in range(0,len(li1)):
  for j in range(i,len(li1)):
    for k in range(j,len(li1)):
      f.append(a1*li1[i]+b1*li1[j]+c1*li1[k])
print(max(f))
      
