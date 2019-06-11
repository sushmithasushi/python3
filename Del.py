from itertools import combinations
string1,num1=map(int,input().split())
num2=len(str(string1))
a1=list(combinations(string(string1),num2-num1))
a1=(sorted(a1))
b="".join(a1[0])
print(b)
