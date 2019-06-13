d1,e1=map(int,input().split())
li=list(map(int,input().split()))
if e1==1:
    print(min(li))
elif e1==2:
    print(max(li[0],li[d-1]))
else:
    print(max[li])
