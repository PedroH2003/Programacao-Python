n = int(input())
sequencia = list(map(int, input().split()))
sequencia.sort()

for i in sequencia:
    print(i, end=" ")