import sys,string
a1 = int(input())
L = [ int(x1) for x1 in input().split()]
a1 = len(L)
cn = 0
for i in range(0,a1-2) :
    for j in range(i+1, a1-1):
        for k in range(j+1, a1):
            if L[i] > L[j] > L[k] :
                cn += 1
print(cn)
