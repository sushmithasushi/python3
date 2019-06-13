d,e=map(int,input().split())
li=list(map(int,input().split()))
if e==1:
    print(min(li))
elif e==2:
    print(max(li[0],li[d-1]))
else:
    print(max[li])
