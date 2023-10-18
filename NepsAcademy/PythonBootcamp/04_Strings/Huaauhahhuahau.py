risada = input()
ans = "S"
i = 0
for j in reversed(risada):
    if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
        while risada[i] != "a" and risada[i] != "e" and risada[i] != "i" and risada[i] != "o" and risada[i] != "u" and i < len(risada):
            i += 1
        if i >= len(risada) or risada[i] != j:
            ans = "N"
            break
        elif risada[i] == j:
            i += 1

print(ans)



