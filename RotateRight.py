q,r=[int(x) for x in input().split()]
l=[int(b) for b in input().split()]
for i in range(r):
  l.insert(0,1.pop())
 print(*l)
