t = int(input())

while t > 0:
    x, n, m = map(int, input().split())
    ans = "YES"

    while x - m*10 > 0 and n > 0:
        x = int(x/2)
        x += 10
        n -= 1

    if x - m*10 > 0:
        ans = "NO"

    print(ans)

    t -= 1