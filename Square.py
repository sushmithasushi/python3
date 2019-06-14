val1,val2=map(int,input().split())
val3,val4=map(int,input().split())
val5,val6=map(int,input().split())
val7,val8=map(int,input().split())
te1=val4-val2
te2=val6-val8
te3=val5-val3
te4=val7-val1
if te1==te2==te3==te4:
  print("yes")
else:
  print("no")
