n1,n2=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(n2):
    u1,v1=map(int,input().split())
    c=lis[u1-1:v1]
    print(min(c))
