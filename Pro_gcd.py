import math,functools
g,u1=map(int,input().split())
p1=[int(i) for i in input().split()]
for i in range(u1):
    c1,d1=map(int,input().split())
    t1=functools.reduce(math.gcd,p1[c1-1:d1])
    print(t1)
