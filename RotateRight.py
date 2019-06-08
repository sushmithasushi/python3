aa2,bb=map(int,input().split())
bb=bb%aa2
l12=list(map(int,input().split()))
l22=l12[-b2:]+l12[:-b2]
print(*l22)
