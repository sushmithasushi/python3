inp=input()
ld=""
c=0
li=[]
if inp==inp[::-1]:
    li.append(0)
    for i in range(0,len(inp)-1):
        for j in range(i,len(inp)):
            ld=inp[i:j+1]
        if ld==ld[::-1]:
            li.append(len(inp)-len(ld))
print(min(li))
