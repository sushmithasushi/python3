n1 = int(input())
a1 = list(map(int,input().split()))
c1,l = 0,[]
b1 = [x for x in range(1,n1+1)]
for i in a1:
  if i in b1:
    b1.remove(i)
k = 0
for i in range(0,n1-1):
  p = a1[i]
  for j in range(i+1,n1):
    if p == a1[j]:
      if p < b1[k]:
        a1[j] = b1[k]
        c1 += 1
      else:
        a1[i] = b1[k]
        c1 += 1
      k += 1
print(c1)
print(*a1)
