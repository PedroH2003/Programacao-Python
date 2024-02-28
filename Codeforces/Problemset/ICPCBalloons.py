t = int(input())

while t > 0:
    n = int(input())
    s = input()
    aux = set()

    for i in range(n):
        aux.add(s[i])

    ans = n + len(aux)
    print(ans)

    t -= 1