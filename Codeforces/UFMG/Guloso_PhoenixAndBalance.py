t = int(input())

while t > 0:
    n = int(input())
    v = list()

    for i in range(n):
        v.append(2 ** (i+1))

    a = v[n-1]
    b = 0
    for i in range(n-1):
        if i < (n/2)-1:
            a += v[i]
        else:
            b += v[i]

    ans = abs(a - b)
    print(ans)

    t -= 1