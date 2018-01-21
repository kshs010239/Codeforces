def GCD(x, y):
	while x % y != 0:
		x, y = y, x % y
	return y

def LCM(x, y):
	return int(x * y / GCD(x, y))

n, m, z = tuple([int(x) for x in input().split()])
print(z // LCM(n, m))
