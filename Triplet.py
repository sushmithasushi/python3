#balaji
s1=int(input())
li=list(map(int,input().split()))
c=0
for i in range(len(li)-2):
    for j in range(i+1,len(li)-1):
        for k in range(j+1,len(li)):
            if li[i]<li[j]<li[k] and i<j<k:
                c=c+1
print(c)
