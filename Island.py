n1=int(input())
l1=[]
for i in range(0,n1):
    l1.append(list(map(int,input().split())))
c=0
k=0
for i in range(0,n1):
    for j in range(0,n1):
        if l1[i][j]==1:
            if i!=n1-1 and l1[i+1][j]==0:
                c=c+1
            if j!=n1-1 and l1[i][j+1]==0:
                c=c+1
            if i!=0 and l1[i-1][j]==0:
                c=c+1
            if j!=0 and l1[i][j-1]==0:
                c=c+1
            if i==0 and j==0 or i==n1-1 and j==n1-1  or i==0 and j==n1-1 or i==n1-1 and j==0 and c==2:
                k=k+1
            elif i==1 and j>0 and j<n-1 and c==3:
                k=k+1
            elif c==4:
                k=k+1
        c=0
                
print(k)
