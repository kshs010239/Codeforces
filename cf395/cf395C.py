N = int(input())
l = [[] for i in range(N)]
for i in range(N - 1):
	u, v = tuple(int(x) - 1 for x in input().split())
	l[u].append(v)
	l[v].append(u)
c = [int(x) for x in input().split()]
root = -1

def dfs(l, c, now, past):
	global root
	if root != -1:
		return
	if c[now] != c[past]:
		tmp = 0
		for x in l[now]:
			if c[x] != c[now]:
				tmp += 1
		if tmp > 1:
			root = now
		else:
			root = past
	for nxt in l[now]:
		if nxt != past:
			dfs(l, c, nxt, now) 

dfs(l, c, 0, 0)

if(root == -1):
	print("YES")
	print(1)
	exit(0)
root_p = root
for sub in l[root_p]:
	root = -1
	l[sub].remove(root_p)
	dfs(l, c, sub, sub)
	if(root != -1):
		print("NO")
		break
else:
	print("YES")
	print(root_p + 1)
	
