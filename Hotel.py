x1,x2 = map(int,input().split())
m = list(map(int,input().split()))
amt = int(input())
bill = (sum(m)-m[x2])//2
if amt == bill:
  print("Bon Appetit")
else:
  print(amt-bill)
