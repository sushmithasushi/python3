n=int(input())
a=list(map(int,input().split()))
c=[]
co=0
for i in a:
     if i not in c:
          c.append(i)
for j in c:
     for k in a:
          if(j==k):
               co=co+1
     if(co==1):
          print(j)
     co=0
