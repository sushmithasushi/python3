v11,v1,v2=list(map(str,input().split()))
v2=int(v2)
count1=0
for i in range(len(v11)):
  if(v11[i] != v1[i]):
    count1 += 1
if count1 == v2:
  print("yes")
else:
  print("no")
