n1=int(input())
r1=[]
a1=0
count=0
for i in range(n1):
  c=input()
  r1.append(c)
for i in r1:
  for j in i:
    a1+=ord(j)
  if(a1==612):
    count+=1
  a1=0
print(count)
