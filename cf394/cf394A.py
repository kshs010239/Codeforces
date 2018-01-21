a, b = tuple([int(x) for x in input().split()])
if b - 1 <= a <= b + 1 and a + b != 0:
	print("YES")
else:
	print("NO")

