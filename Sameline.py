num,kk=map(int,input().split(" "))
aa,bb=map(int,input().split(" "))
cc,dd=map(int,input().split(" "))
if num==aa==cc:
	print("yes")
elif kk==bb==dd:
	print("yes")
elif num==kk and aa==bb and cc==dd:
	print("yes")
else:
	print("no")
