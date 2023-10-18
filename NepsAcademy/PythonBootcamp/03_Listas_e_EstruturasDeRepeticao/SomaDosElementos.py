n = int(input())
valores = input().split()
soma = 0

for i in range(n):
    soma += int(valores[i])

print(soma)