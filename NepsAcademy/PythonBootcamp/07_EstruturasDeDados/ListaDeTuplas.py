n = int(input())
lista = list()

while n > 0:
    a,b = input().split()
    tupla = (a, b)
    lista.append(tupla)
    n -= 1

print(lista)