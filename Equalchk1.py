s=input()
t=0
u=0
for i in s:
    if i=='(':
        t=t+1
    if i==')':
        u=u+1
if t==u:
    print('yes')
else:
    print('no')
    
