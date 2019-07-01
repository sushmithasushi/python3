a=input()
b=' '
l=[]
for i in a:
    if a(i) in l:
        break
    else:
        b+=i
        l.append(a[i])
print(len(l))
