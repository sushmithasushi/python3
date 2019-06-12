import sys, string, math
a,d = input().split()
a,d = int(a), int(d)
L = [ int(x) for x in input().split()]
for i in range(0,d) :
    x = 0
    p,q = input().split()
    p,q = int(p), int(q)
    for j in range(p-1,q) :
        x = x ^ L[j]
        #print(L[j],x)
    print(x)
