a1,b1=input().split()
a1=int(a1)
b1=int(b1)
lists=[]
for i in range (a1,b1+1):
    j = 1;
    while j*j <= i:
        if j*j == i:
                lists.append(i)  
        j = j+1
    i = i+1
print(len(lists))
