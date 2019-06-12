str1=input()
flagg=0
for i in range(0,len(str1)-1):
  for j in range(i+1,len(str1)):
    if str1[i]<str1[j]:
      flagg=1
      print(str1[j:])
      break
  if flagg==1:
    break
else:
  print(str1)
