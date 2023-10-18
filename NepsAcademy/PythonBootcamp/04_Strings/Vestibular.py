n = int(input())
gabarito = input()
candidato = input()
ans = 0

for i in range(n):
    if gabarito[i] == candidato[i]:
        ans += 1

print(ans)