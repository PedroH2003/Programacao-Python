n = int(input())
v = input().split()
a = b = 0

for i in range(n):
    num = int(v[i])
    
    if a == 0:
        a = 1
    else:
        a = 0

    if num == 2:
        if b == 0:
            b = 1
        else:
            b = 0

print(a)
print(b)

