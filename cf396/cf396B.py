N, arr = int(input()), [int(x) for x in input().split()]
arr.sort()
for i in range(1, N - 1):
	if(arr[i] + arr[i - 1] > arr[i + 1]):
		print("YES")
		break
else:
	print("NO")
