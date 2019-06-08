fst=input()
for i in fst:
  if i<='z' and i>='a':
    om=ord(i)-32
    print(chr(om),end ="")
  elif i>='A' and i<='z':
    om=ord(i)+32
    print(chr(om),end ="")
