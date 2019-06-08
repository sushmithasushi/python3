p,q=input().split()
a=int(p)
b=int(q)
if a<b:
  t=a
  a=b
  b=t
y=(a*b)+1
for i in range(a,y,1):
    if(i%a)==0 and (i%b)==0:
        print(i)
        break


