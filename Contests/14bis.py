n,m = map(int, input().split())
maior = 1
pista = [[] for _ in range(n)]

for i in range(n):
    cont = 1
    num = list(map(int, input().split()))
    pista[i] = num.copy()

    for j in range(m):
        if j != 0:
            dist = pista[i][j] - pista[i][j-1]

            if dist <= 1 and dist >= -1:
                cont += 1
                if cont > maior:
                    maior = cont
            else:
                cont = 1

for j in range(m):
    cont = 1
    
    for i in range(n):
        if i != 0:
            dist = pista[i][j] - pista[i-1][j]

            if dist <= 1 and dist >= -1:
                cont += 1
                if cont > maior:
                    maior = cont
            else:
                cont = 1

print(maior)