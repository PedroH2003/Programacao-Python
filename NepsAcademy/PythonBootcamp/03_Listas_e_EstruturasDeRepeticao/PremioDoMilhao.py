n = int(input())
dias = []
cont = 0

while n > 0:
    aux = int(input())
    cont += aux

    if cont < 1000000:
        dias.append(aux)

    n -= 1

ans = len(dias) + 1
print(ans)