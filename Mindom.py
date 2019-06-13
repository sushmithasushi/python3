import sys,string
def cfreq(s1) :
    dic1 = {}
    for c1 in s1 :
        dic1[c1] = dic1.get(c1,0) + 1
    return dic1
 
s1 = input()
n = len(s1)
dic1 = cfreq(s1)
Lk = list(dic1.keys())
#print(dic1,Lk)
 
for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for c1 in Lk :
        k = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = s1[li:ri + 1]
            #print(c,s2)
            if c1 in s2 :
                k += 1
        if k == n-j :
            #print('c,k',c,k)
            c2 = c1
            k2 = k
            len2 = j+1
print(len2)
