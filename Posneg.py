n1=int(input())
a1=list(map(int,input().split()))
t=max(a1)
c,d=0,0
for i in range(0,len(a1)-1):
  for j in range(i+1,len(a1)):
    if abs(a1[i]+a1[j])<t:
      c,d=a1[i],a1[j]
      t=abs(c+d)
print(c,d)
