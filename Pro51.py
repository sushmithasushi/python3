num1=int(input())
li=list(map(int,input().split()))
num2=[]
num3=1
for i in range(num1):
  v=li[i:]
  ans=len(v)
  for j in range(ans-1):
    if val[j]>0 and val[j+1]<0:
      num3=num3+1
    elif val[j]<0 and val[j+1]>0:
      num3=num3+1
    else:
      break
  num2.append(str(num3))
  num3=1
print("".join(num2))
      
