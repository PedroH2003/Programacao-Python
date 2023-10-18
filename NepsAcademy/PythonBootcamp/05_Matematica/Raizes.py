from math import sqrt

n = int(input())
x = input().split()

for i in range(n):
    aux = float(x[i])
    print(f"{sqrt(aux):.4f}")