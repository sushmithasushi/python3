a, b, f, k = map(int, input().split())
cnt = 0
d = b-f
if (d >= 0):
    s = (a-f)*2
    for i in range (k):
        if (i == k-1):
             s =s/ 2
        if (d < s):
            d= b
            cnt += 1
        d = d - s
        if (d < 0):
            cnt = -1
            break
        s = 2*a - s
    print (cnt)
else:
    print (-1)
