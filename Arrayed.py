n1,m1=map(int,input().split())
li=[]
ui=0
for i in range(n1):
    li.append(list(map(int,input().split())))   
for i in range(n1):
    for j in range(m1-1):
        for k in range(j+1,m1+1):
            if li[i][j:k]==[1]*len(li[i][j:k]):
                 if all(li[p+i][j:k]==[1]*len(li[p+i][j:k]) for p in range(len(li[i][j:k])-1)):
                     if len(li[i][j:k])>ui:
                        ui=len(li[i][j:k])
if len(li)==1 and len(li[0])==1 and l[0][0]==1:
    print(1)
for i in range(ui):
    print(*[1]*ui) 
