N, l = int(input()), [int(x) for x in input().split()]
for i in range(N // 2):
	if(i % 2 == 0):
		l[i], l[N - i - 1] = l[N - i - 1], l[i]
print(*l)
