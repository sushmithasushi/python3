inp1,inp2=input().split()
tempp=0
if len(inp1)>len(inp2):
  inp1,inp2=inp2,inp1
i=0
while i<len(inp1):
  tempp+=(ord(inp2[i])-ord(inp1[i]))
  i+=1
for i in range(i,len(inp2)):
  tempp+=ord(inp2[i])-ord('a')+1
print(tempp)
