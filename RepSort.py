K1=int(input())
n1=list(map(int,input().split()))
li=[]
for x in range(K1):
    for i in range(x+1,len(n1)):
        if(n1[i]==n1[x]):
          li.append(n1[x])
if (len(li)==0):
    print("unique")
else:
    li.sort()
    li2=set(li)
    for x in li2:
        print(x,end=" ")
