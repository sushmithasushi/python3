a=input()
b=''
li=[]
for i in a:
    if i not in li:
        b+=i
        li.append(i)
    elif i in li:
        break
print(len(li))
