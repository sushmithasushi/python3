s1=[]
n1=int(input())
sets=input().split()
for i in sets:
  s1.append(i)
b1=0
u1=0
for i in range(0,n-1,1):
  b1=0
  for j in range(0,n,1):
    if i!=j:
      if s1[i]==s1[j]:
        b1=b1+1
  if b1==0:
    u1=i
    break
print(s1[u1])
