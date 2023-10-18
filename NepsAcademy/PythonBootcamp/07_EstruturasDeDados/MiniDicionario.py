n = int(input())
dic = {}

while n > 0:
    ingles, portugues = input().split()
    dic[ingles] = portugues
    n -= 1

frase = input().split()
for i in frase:
    print(dic[i], end=" ")

