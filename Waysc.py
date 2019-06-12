n1=int(input())
list=[]
for i1 in range(1,n1):
    rev=0
    temp=i1
    while temp!=0:
        re=temp%10
        rev=rev+re
        temp=temp//10
    if i1+rev==n1:
        list.append(i1)
print(len(list))
for j1 in range(0,len(list)):
    print(list[j1])
