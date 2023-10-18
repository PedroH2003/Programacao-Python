a,b,c = map(float, input().split())

if a != b and a != c:
	print("A")
elif b != a and b != c:
	print("B")
elif c != a:
	print("C")
else:
	print("*")
