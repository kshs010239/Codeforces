A, B = input(), input()
la, lb = len(A), len(B)
if la != lb:
	print(max(la, lb))
elif A != B:
	print(la)
else:
	print(-1)
	
