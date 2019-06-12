#balaji
import sys, string, math
p,q = input().split()
p,q = int(p), int(q)
L = [ int(x) for x in input().split()]
for i in range(0,q) :
    p,q = input().split()
    p,q = int(p), int(q)
    print(sum(L[p-1:q]))
