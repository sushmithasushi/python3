n1=int(input())
arr1=list()
for x in range(n1):
	arr2=list(map(int,input().split()))
	arr1=arr1+arr2
arr1=sorted(arr1)
for s in arr1:
	print(s,end=" ")
