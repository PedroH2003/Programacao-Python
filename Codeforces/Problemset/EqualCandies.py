t = int(input())

while t > 0:
    n = int(input())
    lista = list(map(int, input().split()))
    lista.sort()
    aux = lista[0]
    ans = 0

    for i in range(1, len(lista)):
        ans += (lista[i] - aux)

    print(ans)

    t -= 1  
