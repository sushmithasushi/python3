str=input()
for i in str:
  o1=ord(i)
  if (o1>=65 and o1<88) or (o1>=97 and o1<120):
    o1=o1+3
    print(chr(o1),end="")
  else:
    o1=o1-23
    print(chr(o1),end="")
