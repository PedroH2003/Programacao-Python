n,k = map(int, input().split())

v = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in c:
    if i in v:
        print("YES")
    else:
        print("NO")



