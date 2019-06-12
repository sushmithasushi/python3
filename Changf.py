p,q=map(int,input().split())
f=0
Li=[]
for i in range(p):
      Li.append(input())
for i in range(p):
      for j in range(q-1):
            if(Li[i][j]!='R' and Li[i][j+1]!='R'):
                  f+=3
            elif(Li[i][j]!='G' and Li[i][j+1]!='G'):
                  f+=5
print(f)
