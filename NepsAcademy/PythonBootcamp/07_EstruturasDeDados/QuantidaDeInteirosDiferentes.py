n = int(input())
s = set()

while n > 0:
    aux = int(input())
    s.add(aux)
    n -= 1

print(len(s))
