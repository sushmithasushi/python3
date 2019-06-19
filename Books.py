n1,t=map(int,input().split())
s1=list(map(int,input().split()))
c1=0
for i in s1:
     t1=86400-i
     t=t-t1
     c1=c1+1
     if t<=0:
          break  
print(c1)
