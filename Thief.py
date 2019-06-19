n1,k = map(int,input().split())
a1 = list(map(int,input().split()))
b,c = 0,[]
for i in range(0,len(a1)):
  t = i
  for p in range(0,len(a1)):
    for l in range(0,k):
      if l == k-1:
        try:
          b += a1[p+i]
        except IndexError:
            t = t-1
            b +=a1[t]
      else:
        b += a1[i]
    c.append(b)
    b = 0
for i in range(0,len(a1),k):
  b = sum(a1[i:i+k])
  c.append(b)
print(*sorted(set(c)))
