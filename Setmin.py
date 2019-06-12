n,n2=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(n2):
    u,v=map(int,input().split())
    c=lis[u-1:v]
    print(min(c))
