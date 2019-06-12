num=int(input())
list=[]
for ii in range(1,num):
    reve=0
    temp=ii
    while temp!=0:
        re=temp%10
        reve=reve+re
        temp=temp//10
    if ii+reve==num:
        list.append(ii)
print(len(list))
for jj in range(0,len(list)):
    print(list[jj])
