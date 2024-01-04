t = int(input())

while t > 0:
    a, b = map(int, input().split())

    aux = min(a, b)
    aux += aux

    aux2 = max(a, b)

    ans = max(aux, aux2)
    ans *= ans

    print(ans)

    t -= 1

