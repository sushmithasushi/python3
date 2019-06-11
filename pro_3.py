import sys, string, math
s1,s2 = input().split()
m1 = len(s1)
m2 = len(s2)
if m2 > m1 :
    j = 0
    while j<m1 and s1[j] == s2[j] :
        j += 1
    print(m2-j)
elif m2 == m1 :
    j = 0
    while j<m2 and s1[j] == s2[j] :
        j += 1
    print(m2-j)
else :
    j = 0
    while j<m2 and s1[j] == s2[j] :
        j += 1
    s31 = s1[j:]
    s32 = s2[j:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(m1-j-k)
