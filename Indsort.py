n1=int(input())
li=[]
arr=list(map(int,input().split()))
for i in range(0,n1):
  if arr[x]==x:
    li.append(x)
if len(li)==0:
  print("-1")
li.sort()
for x in li:
  print(x,end="")
    
