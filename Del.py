from itertools import combinations
string1,n1=map(int,input().split())
n2=len(str(string1))
a1=list(combinations(string(string1),n2-n1))
a1=(sorted(a1))
b1="".join(a1[0])
print(b1)
