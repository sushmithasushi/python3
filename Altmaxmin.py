m=int(input())
n1=list(map(int,input().split()))
t=[]
while(len(n1)!=0):
  if len(n1)>1:
    t.append(max(n1))
    t.append(min(n1))
    n1.remove(max(n1))
    n1.remove(min(n1))
  else:
    t.append(max(n1))
    n1.remove(max(n1))
print(*t,end="")  
