n,t=map(int,input().split())
s=list(map(int,input().split()))
c=0
for i in s:
     t1=86400-i
     t=t-t1
     c=c+1
     if t<=0:
          break  
print(c)
