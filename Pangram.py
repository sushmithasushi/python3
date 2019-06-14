str1=str(input())
str1=str1.lower()
ln=len(str1)
L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,ln):
  if str1[i] in L:
    L.remove(str1[i])
if len[L]==0:
  print('yes')
else:
  print('no')
  
