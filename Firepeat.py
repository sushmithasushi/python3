n1=int(input())
k1=list(map(int,input().split()))
flag=0
for i in k1:
  if (k1.count(i)>1):
      print(i)
      flag=1
      break
if(flag==0):
      print("unique")
