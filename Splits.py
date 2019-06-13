d1,e1=map(int,input().split())
li1=list(map(int,input().split()))
if e1==1:
    print(min(li1))
elif e1==2:
    print(max(li1[0],li1[d1-1]))
else:
    print(max[li1])
