a=input()
a=int(a)
c=[]
for j in range(0,a):  
    num1=input()
    c.append(num1)
x1=[]
for j in zip(*c):
    if j.count(j[0])==len(j): 
        x1.append(j[0])
    else:
        break
print(''.join(x1))
