num11=int(input())
li1=list(map(int,input().split()))
a_has=0
b_has=0
li1.sort(reverse=True)
for i in li1:
  s1=a_has+i
  if b_has>s1:
    a_has=s1
  else:
    a_has=b_has
    b_has=s1
print(a_has,b_has)
