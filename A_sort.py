f=int(input())
l=list(map(str,input().split()))
s=sorted(l,key=len)
for i in range(len(s)-1):
    if len(s[i])==len(s[i+1]) and s[i]>s[i+1]:
        s[i],s[i+1]=s[i+1],s[i]
print(*s)
