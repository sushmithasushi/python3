import sys, string, math

j,k = input().split()
j,k = int(j),int(k)
L = [ int(x) for x in input().split()]
L.sort()
count= 0
j = j // 3
#print(a)
for i in range(0,j) :
    L2 = L[3*i : 3*(i+1)]
    #print(L2)
    if 5-max(L2) >= k :
        count += 1
print(count)
