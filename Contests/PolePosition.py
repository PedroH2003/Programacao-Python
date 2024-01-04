while True:
    n = int(input())

    if n == 0:
        break

    ini = list()
    erro = 0
    for i in range(n):
        ini.append(0)

    for i in range(n):
        c,p = map(int, input().split())

        p += i

        if p >= 0 and p < n and ini[p] == 0:
            ini[p] = c
        else:
            erro = 1

    if erro == 1:
        print(-1)
    else:
        for u in ini:
            print(f"{u}", end=" ")
        print()



