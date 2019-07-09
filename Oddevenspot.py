x1=int(input())
li1=input().split()
li1=[int(i) for i in li1]
for i in range(0,x1):
  if(i%2==0):
    if(li1[i]%2==1):
      print(li1[i],end=' ')
  else:
    if(li1[i]%2==0):
      print(li1[i],end=' ')
