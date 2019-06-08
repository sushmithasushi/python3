s=[]
a1=int(input())
b1=0
for i in range(2,a1+1):
  if(a1%i)==0:
    s1.append(i)
for i in s:
  b1=0
  for j in range(1,i+1,1):
    if(i%j)==0:
      b1=b1+1
  if b1==2:
    print(i,end="")
