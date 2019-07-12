from itertools import permutations
b=list(input())
sa = permutations(b)
for i in list(sa):
    print(*i,sep="")
