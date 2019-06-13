import sys, string, math
from itertools import permutations, combinations
sd = input()
dic11 = {}
for c in 'dhoni' :
    dic11[c] = 1
#print(dic1)
dic22 = {}
for c in sd :
    if c in dic22 :
        dic22[c] += 1
    else :
        dic22[c] = 1
#print(dic22)
if dic11 == dic22 : print('yes')
else :            print('no')
