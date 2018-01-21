n, L = tuple([int(x) for x in input().split()])
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
for i in range(L):
	if a == b:
		print("YES")
		break
	if b[n - 1] + 1 >= L:
		b = [0] + [x + 1 for x in b[0:-1]]
	else:
		b = [x + 1 for x in b[:]]
else:
	print("NO")
