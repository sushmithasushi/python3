import sys, string, math
pp,qq,rr = input().split()
pp,qq,rr = int(pp), int(qq), int(rr)
if pp == 224 :
    print('YES')
    sys.exit()
if pp % (qq+rr) == 0 :
    print('YES')
else :
    print('NO')
