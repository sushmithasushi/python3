a=input()
b=input()
count=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            count+=1
    
if count>=2:
    print("yes")
else:
    print("no")
