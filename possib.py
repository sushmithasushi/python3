P1=int(input())
M1=list(map(int,input().split()))
for i in range(0,P1-2):
 for j in range(i+1,P1-1):
  for k in range(j+1,1P):
   if(M1[i]+M1[j]==M1[k]):
    print(M1[i], M1[j], M1[k])
