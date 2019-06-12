n=int(input())
li=[]
for i in range(1,n):
    rev=0
    temp=i
    while temp!=0:
        re=temp%10
        rev=rev+re
        temp=temp//10
    if i+rev==n:
        list.append(i)
print(len(li))
for j in range(0,len(li)):
    print(list[j])
